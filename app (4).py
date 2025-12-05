
import streamlit as st
import os
import requests
pip install agno
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools
from agno.models.google import Gemini
from datetime import datetime

# -----------------------
# 🔑 API KEYS
# -----------------------
SCRAPER_API_KEY = os.environ.get("SCRAPER_API_KEY", "97ce36403e090db482b513ac7e6d6bd232a3ed23bf028ebb1951670f9c36d5a4")
SERPAPI_KEY = os.environ.get("SERPAPI_KEY", "a5f76e676a90b536a7d2c167e0a48bf8")

# -----------------------
# 🌍 STREAMLIT UI
# -----------------------
st.set_page_config(page_title="🌍 AI Travel Planner", layout="wide")
st.markdown('<h1 style="text-align:center; font-size:36px; color:#ff5733;">✈️ AI-Powered Travel Planner</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:20px; color:#555;">Plan your dream trip with AI!</p>', unsafe_allow_html=True)

# -----------------------
# 📌 USER INPUTS
# -----------------------
st.markdown("### 🌍 Where are you headed?")
source = st.text_input("🛫 Departure City (IATA Code):", "BOM")
destination = st.text_input("🛬 Destination (IATA Code):", "DEL")

st.markdown("### 📅 Plan Your Adventure")
num_days = st.slider("Trip Duration (days):", 1, 14, 5)

travel_theme = st.selectbox(
    "🎭 Select Your Travel Theme:",
    ["💑 Couple Getaway", "👨‍👩‍👧‍👦 Family Vacation", "🏔️ Adventure Trip", "🧳 Solo Exploration"]
)

activity_preferences = st.text_area(
    "🌍 What activities do you enjoy?",
    "Relaxing on the beach, exploring historical sites"
)

departure_date = st.date_input("Departure Date")
return_date = st.date_input("Return Date")

# (Paste the rest of your Streamlit AI Travel Planner code here)
