import streamlit as st
from user_registration import register_user
from user_authentication import authenticate_user

def main():
    st.sidebar.title("Voice Authentication App")

    menu = ["Register User", "Authenticate User"]
    choice = st.sidebar.radio("Navigation", menu)

    if choice == "Register User":
        register_user()
    elif choice == "Authenticate User":
        authenticate_user()

if __name__ == "__main__":
    main()
