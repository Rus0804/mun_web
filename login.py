import streamlit as st

# Simulate a simple user database with roles
USER_CREDENTIALS = {
    "admin_user": {"password": "admin_pass", "role": "admin"},
    "candidate_user": {"password": "candidate_pass", "role": "candidate"},
    "hirer_user": {"password": "hirer_pass", "role": "hirer"},
}

# Function to check login credentials
def check_login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username]["password"] == password:
        return USER_CREDENTIALS[username]["role"]
    return None

# Function to render the login page
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        role = check_login(username, password)
        if role:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['role'] = role
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to render the admin page
def admin_page():
    st.title(f"Welcome Admin, {st.session_state['username']}!")
    st.write("This is the admin page.")
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.session_state['role'] = ""
        st.experimental_rerun()

# Function to render the candidate page
def candidate_page():
    st.title(f"Welcome Candidate, {st.session_state['username']}!")
    st.write("This is the candidate page.")
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.session_state['role'] = ""
        st.experimental_rerun()

# Function to render the hirer page
def hirer_page():
    st.title(f"Welcome Hirer, {st.session_state['username']}!")
    st.write("This is the hirer page.")
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.session_state['role'] = ""
        st.experimental_rerun()

# Main app logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""
    st.session_state['role'] = ""

if st.session_state['logged_in']:
    if st.session_state['role'] == "admin":
        admin_page()
    elif st.session_state['role'] == "candidate":
        candidate_page()
    elif st.session_state['role'] == "hirer":
        hirer_page()
else:
    login_page()
