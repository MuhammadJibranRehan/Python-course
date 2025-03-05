import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker", page_icon=("🌘"), layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {text-align: centre;}
    .stTextInput {width: 100%; !important; margin: auto;}
    .stButton button {width: 100%; background-color: lightblue; color: black; font-size: 18px;}
    .stButton button:hover {background-color: lightgray; color: black;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.header("🔐 Password Strength Generator By Kinza")
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) > 8:
        score += 1  # Increased score by 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Check uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **uppercase (A-Z) and lowercase (a-z) letters**.")

    # Check if password contains a digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one digit (0-9)**.")

    # Check if password contains a special character
    if re.search(r"[!#@$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **one special character (!#@$%^&*)**.")

    # Display password strength results
    if score >= 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score >= 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding some security features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestion below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve your password**"):
            for item in feedback:
                st.write(item)

# Input field for password
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

#Add a small spacing fix
st.markdown("<style>div.stButton { margin-top: -10px; }</style>",unsafe_allow_html=True)

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")  # Show warning if password is empty