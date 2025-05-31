const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const bodyParser = require('body-parser');
const path = require('path');
const cors = require('cors');

const app = express();
app.use(cors());

const db = new sqlite3.Database('./users.db');
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname)));

// Create users table if not exists
// likes and cart are JSON strings for future use
const userTableSql = `CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  likes TEXT DEFAULT '[]',
  cart TEXT DEFAULT '[]'
)`;
db.run(userTableSql);

// Register endpoint
app.post('/api/register', async (req, res) => {
  const { username, email, password } = req.body;
  if (!username || !email || !password) {
    return res.status(400).json({ error: 'All fields required.' });
  }
  const hash = await bcrypt.hash(password, 10);
  db.run(
    'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
    [username, email, hash],
    function (err) {
      if (err) {
        if (err.message.includes('UNIQUE')) {
          return res.status(409).json({ error: 'Username or email already exists.' });
        }
        return res.status(500).json({ error: 'Database error.' });
      }
      res.json({ success: true, userId: this.lastID });
    }
  );
});

// Login endpoint
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ error: 'All fields required.' });
  }
  db.get(
    'SELECT * FROM users WHERE username = ? OR email = ?',
    [username, username],
    async (err, user) => {
      if (err) return res.status(500).json({ error: 'Database error.' });
      if (!user) return res.status(401).json({ error: 'Invalid credentials.' });
      const match = await bcrypt.compare(password, user.password_hash);
      if (!match) return res.status(401).json({ error: 'Invalid credentials.' });
      res.json({ success: true, userId: user.id, username: user.username });
    }
  );
});

// Like endpoint
app.post('/api/like', (req, res) => {
  const { userId, product } = req.body;
  if (!userId || !product) {
    return res.status(400).json({ error: 'Missing userId or product.' });
  }
  db.get('SELECT likes FROM users WHERE id = ?', [userId], (err, row) => {
    if (err) return res.status(500).json({ error: 'Database error.' });
    if (!row) return res.status(404).json({ error: 'User not found.' });
    let likes = [];
    try {
      likes = JSON.parse(row.likes);
    } catch (e) {
      likes = [];
    }
    if (!likes.includes(product)) {
      likes.push(product);
    } else {
      return res.json({ success: true }); // Already liked
    }
    db.run('UPDATE users SET likes = ? WHERE id = ?', [JSON.stringify(likes), userId], function (err2) {
      if (err2) return res.status(500).json({ error: 'Database error.' });
      res.json({ success: true });
    });
  });
});

// Unlike endpoint
app.delete('/api/like', (req, res) => {
  const { userId, product } = req.body;
  if (!userId || !product) {
    return res.status(400).json({ error: 'Missing userId or product.' });
  }
  db.get('SELECT likes FROM users WHERE id = ?', [userId], (err, row) => {
    if (err) return res.status(500).json({ error: 'Database error.' });
    if (!row) return res.status(404).json({ error: 'User not found.' });
    let likes = [];
    try {
      likes = JSON.parse(row.likes);
    } catch (e) {
      likes = [];
    }
    const newLikes = likes.filter(name => name !== product);
    db.run('UPDATE users SET likes = ? WHERE id = ?', [JSON.stringify(newLikes), userId], function (err2) {
      if (err2) return res.status(500).json({ error: 'Database error.' });
      res.json({ success: true });
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
}); 