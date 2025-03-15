import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Criteria Checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Strength Level
    if score <= 2:
        strength = "Weak"
        color = "#FF4B4B"  # Red
    elif score <= 4:
        strength = "Moderate"
        color = "#FFA500"  # Orange
    else:
        strength = "Strong"
        color = "#4CAF50"  # Green
    
    return strength, color, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if password:
    strength, color, feedback = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
    
    if strength == "Weak":
        st.subheader("⚠ Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")
    
    st.subheader("🔑 Generate a Strong Password:")
    if st.button("Suggest Password"):
        st.write(f"**Try this:** `{generate_strong_password()}`")
