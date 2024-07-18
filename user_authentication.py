import os
import streamlit as st
import numpy as np
import psycopg2
from psycopg2.extras import RealDictCursor
from database import conn
from recording import record_audio
from recognition import recognize_speech
from feature_extraction import extract_features

def authenticate_audio(captured_features, reference_features, threshold=50):
    distance = np.linalg.norm(captured_features - reference_features)
    return distance < threshold

def validate_authentication(auth_text, reg_text, captured_features, reference_features):
    if reg_text == auth_text and authenticate_audio(captured_features, reference_features):
        return True
    else:
        return False

temp_dir = "temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

def authenticate_user():
    st.title("Authenticate User")
    auth_username = st.text_input("Enter your username for authentication").lower()
    if st.button("Record and Authenticate"):
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users WHERE username = %s", (auth_username,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            auth_filename = os.path.join(temp_dir, f"{auth_username}_auth.wav")
            record_audio(auth_filename)
            auth_text = recognize_speech(auth_filename)
            if auth_text:
                st.write(f"**Recognized text:** `{auth_text}`")
                captured_features = extract_features(auth_filename)
                reference_features = np.frombuffer(user["audio_features"], dtype=np.float32)
                reg_text = user["reg_text"]

                if validate_authentication(auth_text, reg_text, captured_features, reference_features):
                    st.success("Authentication successful.")
                else:
                    st.error("Authentication failed.")
                
            else:
                st.error("Authentication failed. Try again.")
        else:
            st.error("User not found.")
