# main.py
import streamlit as st
from pages.projects import render_projects_page
from pages.tasks import render_tasks_page
import os
from dotenv import load_dotenv

def check_environment():
    load_dotenv()
    required_vars = ['SUPABASE_URL', 'SUPABASE_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        st.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        st.write("Please create a .env file in your project root with the following variables:")
        st.code("""
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
        """)
        st.stop()

def main():
    st.set_page_config(page_title="Project Tracker", layout="wide")
    check_environment()
    
    # Initialize session state
    if 'current_project' not in st.session_state:
        st.session_state.current_project = None
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button("Projects"):
        st.session_state.current_project = None
        st.experimental_rerun()
    
    # Main content
    if st.session_state.current_project is None:
        render_projects_page()
    else:
        render_tasks_page(st.session_state.current_project)

if __name__ == "__main__":
    main()