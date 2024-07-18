import os
import streamlit as st
import re
import psycopg2
import numpy as np
from psycopg2.extras import RealDictCursor
from database import conn
from recording import record_audio
from recognition import recognize_speech
from feature_extraction import extract_features

temp_dir = "temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

def register_user():
    st.title("Register User")
    username = st.text_input("Enter your username")
    if re.search(r'[^a-zA-Z0-9]', username):
        st.error("Username can only contain letters and numbers, with no spaces or special characters.")
    else:
        username = username.lower()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            st.warning("Username already registered.")
            if st.button("Record and Re-register"):
                filename = os.path.join(temp_dir, f"{username}_reg.wav")
                record_audio(filename)
                reg_text = recognize_speech(filename)
                if reg_text:
                    st.write(f"**Recognized text:** `{reg_text}`")
                    features = extract_features(filename)
                    cursor = conn.cursor()
                    cursor.execute("UPDATE users SET reg_text = %s, audio_features = %s WHERE username = %s",
                                   (reg_text, features.tobytes(), username))
                    conn.commit()
                    cursor.close()
                    st.success(f"User {username} re-registered successfully!")
                    
                else:
                    st.error("Speech was not recognized. Please re-register again.")
                
        elif st.button("Record and Register"):
            if username:
                filename = os.path.join(temp_dir, f"{username}_reg.wav")
                record_audio(filename)
                reg_text = recognize_speech(filename)

                if reg_text:
                    st.write(f"**Recognized text:** `{reg_text}`") 
                    features = extract_features(filename)
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO users (username, reg_text, audio_features) VALUES (%s, %s, %s)",
                                   (username, reg_text, features.tobytes()))
                    conn.commit()
                    cursor.close()
                    st.success(f"User registered successfully!")
                else:
                    st.error("Speech was not recognized. Please re-register again.")