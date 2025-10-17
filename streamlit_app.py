import streamlit as st

# পেজের কনফিগ
st.set_page_config(page_title="MD Mostafa Niloy - CEO", layout="wide")

# HTML ফাইল ওপেন করে পড়া
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# HTML কনটেন্ট রেন্ডার করা
st.components.v1.html(html_data, height=3000, scrolling=True)

