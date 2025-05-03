# Magic Archive - Chiikawa Merchandise Browser


## 🔧 Setup Instructions (Already set in the local file)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧁 Project Scope  
This project focuses on designing and developing a merchandise browsing platform based on the popular Japanese animation *Chiikawa*. The platform allows users to explore characters from the *Chiikawa* universe, view detailed character and product information, and save favorite merchandise.  

Core components include:
- A homepage with filtering options  
- Individual character profile pages  
- Interactive product pop-ups  
- A favorites collection page  

The project also involves creating a solid information architecture and converting Figma designs into functional HTML using [Cursor](https://cursor.sh).

---

## 🎯 Target Users  
The target users are fans of the *Chiikawa* animation series who are interested in discovering, collecting, and potentially purchasing themed merchandise. These users are likely to value:
- Character storytelling  
- Aesthetic visual design  
- A smooth and well-organized browsing experience  

---

## ✨ Features  

- **Homepage**  
  - Large promotional banner featuring all *Chiikawa* characters  
  - Character cards with filter functionality  
  - Each card includes: image, name, introduction, release date, and movie/episode name  

- **Character Page**  
  - Full character information  
  - Related merchandise cards  
  - Filtering by release date and type  
  - Favorite button for each item  

- **Favorites Page**  
  - Displays all items the user has favorited  
  - Easy access to liked products  

- **Product Pop-up**  
  - Opens on click  
  - Shows: product image, name, price (with price trend), and reference purchase links  

---

## 🗓️ Timeline  

| Date Range     | Task                                                              |
| -------------- | ----------------------------------------------------------------- |
| April 11–18    | Information architecture                                          |
| April 18–25    | Low-fidelity wireframes                                           |
| April 25–May 2 | High-fidelity prototypes                                          |
| **May 2–9**    | **Homepage, product pop-up, and product detail page development** |
| May 9–16       | Character page development                                        |
| May 16–23      | Favorites page & interactive logic                                |
| May 23–30      | Final iteration and refinement                                    |


---

## 📬 Contact  

For more details or project inquiries, please contact:  
Yunqing Zhao Client Email: yzhao73@uw.edu
Shangming Zhuo Developer Email: oiviauw@uw.edu  
GitHub Repo: [https://github.com/LydiaZZzzz/Collector-land](https://github.com/LydiaZZzzz/Collector-land)

---

## 📌 Progress Log

| Date  | Progress                                                                 |
| 4.18 | Completed the planned information architecture, including user flows and core page structure. Initiated homepage development ahead of schedule using Streamlit. Created initial file and folder organization (`static/`, `webhomepage.py`, `requirements.txt`). Implemented a top navigation bar with fixed positioning and clickable buttons. Designed and overlaid interactive product hover dots on a visual banner. Documented setup instructions and development status clearly in `README.md`.                                                                                              |
| 5.2  | Finished development of three key interfaces: `home.html`, `search.html`, and `product-detail.html`. Implemented a functional search bar on the homepage that navigates to the product pop-up. Built a product pop-up window with two working buttons: one for reshuffling products and one for returning to the homepage. Completed the product detail page layout, including a large image display and three-view switching feature. Also wrote an initial test file (`product-detail.test.js`) and resolved git push errors by submitting code via a protected-branch pull request from `dev`. |
| Next | Planned for 5.9: Start character page development and integrate favorite toggling logic. Improve UI feedback (e.g. loading animations) and apply initial usability fixes based on internal testing.                                                                                                                                                                                                                                                                                                                                                                                               |


