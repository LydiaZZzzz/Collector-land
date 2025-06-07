# 🧙‍♀️ Magic Archive - Chiikawa Merchandise Browser

A merchandise exploration platform built around the beloved Japanese animation *Chiikawa*. This project allows fans to search for themed products using key character attributes and interact with product pop-ups and detail views in a smooth, visually engaging environment.

---

## 🔧 Setup Instructions

Make sure you have Python 3 installed. Then run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧁 Project Scope

This platform was designed and built to:

- Allow fans to explore *Chiikawa* character-themed merchandise  
- Enable fuzzy keyword-based product discovery (e.g., “magic”, “yellow”, “bow”)  
- Present products in an engaging way using interactive pop-ups and detail pages  
- Build a solid foundation for favorites/likes and cart functionalities  

The app is developed using Streamlit and HTML templates, with visuals designed in Figma and translated into code via [Cursor](https://cursor.sh).

---

## 🎯 Target Users

The target audience includes fans and collectors of *Chiikawa* merchandise who are:

- Interested in visual exploration of themed products  
- Motivated by character storytelling and aesthetics  
- Looking for a clean and organized browsing experience  

---

## ✨ Features

### ✅ Implemented (as of June 6)

- **Homepage**
  - Keyword-based search bar (supports fuzzy search)
  - Visual promotional banner with characters
  - Filterable character/product cards  

- **Product Pop-up (generated page)**
  - Displays matched product with image, name, price, and link
  - "Try another match": cycles through other matching products
  - "This is the one": navigates to the full product detail page

- **Product Detail Page**
  - Shows complete product info including:
    - Large product image
    - Detail images
    - Description, material, dimensions, price
    - Official purchase links

- **Favorites (Likes) Page [Basic Version]**
  - Users can favorite products and revisit them in a dedicated view

- **Shopping Cart [Initial Prototype]**
  - Users can add products to a simple cart interface

---

## 🗓️ Project Timeline

| Date Range    | Task Description                                                       |
|---------------|------------------------------------------------------------------------|
| April 11–18   | Planned information architecture, user flows, and basic UI decisions   |
| April 18–25   | Created low-fidelity wireframes for major pages                        |
| April 25–May 2| Built high-fidelity UI in Figma, began HTML template conversion        |
| May 2–9       | Developed homepage, fuzzy search logic, and product pop-up base        |
| May 9–16      | Implemented full search-to-pop-up-to-detail flow, built product pages  |
| May 16–23     | Finalizing favorites/likes and shopping cart functionality             |
| May 23–30     | Iteration, UI polish, usability testing, and documentation             |
| May 30–June 6 | Final bug fixing, responsive design adjustments, feature wrap-up, and handoff preparation |

---

## 📌 Progress Log

| Date  | Progress Summary |
|-------|------------------|
| 4.25  | Completed the planned information architecture, including user flows and core page structure. Initiated homepage development ahead of schedule using Streamlit. Created initial file and folder organization (`static/`, `webhomepage.py`, `requirements.txt`). Implemented a top navigation bar with fixed positioning and clickable buttons. Designed and overlaid interactive product hover dots on a visual banner. Documented setup instructions and development status clearly in `README.md`. |
| 5.9   | Learned how to implement fuzzy search logic; cleaned and structured the product information CSV (`chiikawa_data/products_test.csv`). |
| 5.16  | Implemented search navigation from the homepage to the product pop-up (`generated-page`), allowing key features like “yellow”, “magic”, “bow”, or “magic wand” to trigger matching product pop-ups. Added “Try another match” logic: if other matches exist, another product is shown; if not, the page remains. Built product detail pages for all merchandise including name, main image, detail images, price, material, size, and official links. Enabled navigation from product pop-up to detail page via “This is the one” button. Major features are now complete. |
| 5.23  | Basic versions of Favorites and Shopping Cart pages implemented. Started adding user feedback loop. UI tweaks in response to early testers. |
| 6.1   | Completed responsive layout tuning and final UI polish. Improved page transitions and loading behavior. Performed cross-device testing. |
| 6.6   | **Project officially completed and delivered to the client.** All major planned features implemented. Codebase organized, documented, and submitted with usage instructions. |

---

## 🔮 Future Considerations

The following enhancements are not part of the current handoff but may be considered in future iterations:

- Add persistent local storage or backend for likes/cart memory  
- Polish cart checkout simulation and add email/share options  
- Transition to Streamlit Cloud or other hosting for public access  
- Add internationalization and language switching support  
- Support mobile gestures for navigation and selection

---

## 🧪 How to Test

You can test the keyword search functionality directly from the homepage. Try using inputs such as:

- `yellow`  
- `magic`  
- `bow`  
- `magic wand`  

The system will display a matching product in a pop-up. Use “Try another match” to cycle through related products, or click “This is the one” to go to the full product detail page.

---

## 📬 Contact

For inquiries or collaboration, feel free to reach out:

- **Yunqing Zhao** (Client) – yzhao73@uw.edu  
- **Shangming Zhuo** (Developer) – oiviauw@uw.edu  
- **GitHub Repo** – [https://github.com/LydiaZZzzz/Collector-land](https://github.com/LydiaZZzzz/Collector-land)
