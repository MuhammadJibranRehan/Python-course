import streamlit as st

# Enhanced Styling
st.set_page_config(page_title="Unit Converter", page_icon="🌍", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        body { background-color: #f0f2f6; }
        .stButton button { background-color: #ff4b4b; color: white; }
    </style>
""", unsafe_allow_html=True)

# Conversion Functions
def convert_units(category, from_unit, to_unit, value):
    conversions = {
        "Distance": {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Miles": 1609.34},
        "Temperature": lambda v, f, t: (v * 9/5 + 32) if (f == "Celsius" and t == "Fahrenheit") else (v - 32) * 5/9 if (f == "Fahrenheit" and t == "Celsius") else v,
        "Weight": {"Kilograms": 1, "Grams": 0.001, "Pounds": 2.20462, "Ounces": 35.274},
        "Area": {"Square Meters": 1, "Square Kilometers": 1_000_000, "Square Feet": 0.092903, "Acres": 4046.86, "Hectares": 10_000},
        "Time": {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400},
        "Volume": {"Liters": 1, "Milliliters": 0.001, "Gallons": 3.785, "Cups": 0.24},
        "Speed": {"Meters/Second": 1, "Kilometers/Hour": 3.6, "Miles/Hour": 2.237},
        "Pressure": {"Pascals": 1, "Atmospheres": 101325, "Bar": 100000, "PSI": 6894.76}
    }
    return value * conversions[category][from_unit] / conversions[category][to_unit] if category not in ["Temperature"] else conversions[category](value, from_unit, to_unit)

# UI - Header
st.title("🌍 Unit Converter")
st.subheader("Convert between different units effortlessly!")

# Select Conversion Category
category = st.selectbox("Select Category:", ["Distance", "Temperature", "Weight", "Area", "Time", "Volume", "Speed", "Pressure"])

# Dynamic Unit Selection
unit_options = {
    "Distance": ["Meters", "Kilometers", "Feet", "Miles"],
    "Temperature": ["Celsius", "Fahrenheit"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Area": ["Square Meters", "Square Kilometers", "Square Feet", "Acres", "Hectares"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Volume": ["Liters", "Milliliters", "Gallons", "Cups"],
    "Speed": ["Meters/Second", "Kilometers/Hour", "Miles/Hour"],
    "Pressure": ["Pascals", "Atmospheres", "Bar", "PSI"]
}
from_unit = st.selectbox("From:", unit_options[category])
to_unit = st.selectbox("To:", unit_options[category])

# Real-time Conversion with Slider & Input
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
result = convert_units(category, from_unit, to_unit, value)

# Display result instantly
st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown("🔧 Built with ❤️ by **Muhammad Jibran Rehan**")