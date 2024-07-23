import streamlit as st

# Simulate a simple user database
USER_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2",
}

# Function to check login credentials
def check_login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    return False

# Function to render the login page
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to render the main page after login
def main_page():
    st.title(f"Welcome, {st.session_state['username']}!")
    st.write("This is the main page after login.")
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.experimental_rerun()

# Main app logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""

if st.session_state['logged_in']:
    main_page()
else:
    login_page()
