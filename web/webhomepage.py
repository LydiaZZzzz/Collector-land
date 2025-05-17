import streamlit as st
from PIL import Image
import os

# === Page Config ===
st.set_page_config(page_title="Chiikawa ** CollectorLand", page_icon="🎨", layout="wide")

# === Top Navigation Bar (Sticky) with Refined Layout ===
st.markdown(
    """
    <style>
    .top-nav {
        background-color: #ffffff;
        padding: 10px 30px;
        display: flex !important;
        justify-content: space-between;
        align-items: center;
        height: 50px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 10000;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    .nav-left {
        font-family: 'Georgia', serif;
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        display: block !important;
    }
    .nav-right {
        display: flex !important;
        gap: 12px;
    }
    .nav-right button {
        padding: 6px 16px;
        border: 1px solid #ccc;
        background-color: #ffffff;
        border-radius: 10px;
        cursor: pointer;
        font-size: 14px;
        display: inline-block !important;
    }
    .spacer {
        height: 30px;
    }
    .stApp {
        margin-top: 60px;
    }
    .stImage {
        margin-top: -20px;
        padding-top: 0 !important;
    }
    .block-container {
        padding-top: 0 !important;
    }
    </style>

    <div class="top-nav">
        <div class="nav-left">Chiikawa ** CollectorLand</div>
        <div class="nav-right">
            <button>🎭 Characters</button>
            <button>❤️ Likes</button>
        </div>
    </div>
    <div class="spacer"></div>
    """,
    unsafe_allow_html=True
)

# === Banner Image ===
image_path = "static/banner.png"
if os.path.exists(image_path):
    banner = Image.open(image_path)
    st.image(banner)
else:
    st.warning("🚫 Banner image not found at static/banner.png")

# === Dots with Hover Cards (No Glow) ===
st.markdown("""
<style>
.dot {
  height: 20px;
  width: 20px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  margin: 0 10px;
  position: relative;
}

.card {
  display: none;
  position: absolute;
  top: 30px;
  left: -100px;
  width: 250px;
  padding: 15px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  border-radius: 8px;
  z-index: 999;
  font-size: 14px;
}

.dot:hover .card {
  display: block;
}
</style>
<div style="display:flex; justify-content:center; padding:20px;">
  <div class="dot">
    <div class="card">
      <img src="https://via.placeholder.com/60" style="float:left; margin-right:10px;">
      <b>Chiikawa Mug</b><br>
      <span>💴 ¥1,200 → <b>¥980</b></span><br>
      <a href="#">Buy Now</a>
    </div>
  </div>
  <div class="dot">
    <div class="card">
      <img src="https://via.placeholder.com/60" style="float:left; margin-right:10px;">
      <b>Chiikawa Plush</b><br>
      <span>💴 ¥2,000 → <b>¥1,580</b></span><br>
      <a href="#">Buy Now</a>
    </div>
  </div>
  <div class="dot">
    <div class="card">
      <img src="https://via.placeholder.com/60" style="float:left; margin-right:10px;">
      <b>Chiikawa T-shirt</b><br>
      <span>💴 ¥3,500 → <b>¥2,980</b></span><br>
      <a href="#">Buy Now</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# === Story Summary Section ===
st.markdown("""
## 🧸 Story Summary

**Chiikawa (ちいかわ)**, also known as *Nanka Chiisakute Kawaii Yatsu* (なんか小さくてかわいいやつ, "literally translated to: Something Small and Cute"), is a Japanese manga series written and illustrated by Nagano. 

The main contents of the work are the daily lives and interactions of a series of cute animal or animal-inspired characters. It has been serialized online via Twitter since January 2020 and has been collected in seven tankōbon volumes by Kodansha. 

An anime television series adaptation by Doga Kobo premiered in April, 2022.
""")

# === Bottom Tab with Official Site Link ===
st.markdown("""
<style>
.bottom-tab {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 15px;
    margin-top: 20px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.bottom-tab:hover {
    background-color: #e9ecef;
}

.tab-title {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
}

.tab-description {
    color: #666;
    font-size: 14px;
    margin-top: 8px;
}
</style>

<div class="bottom-tab">
    <div class="tab-title">🌐 Official Site</div>
    <div class="tab-description">👉 Click the icon below to visit the official site</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
