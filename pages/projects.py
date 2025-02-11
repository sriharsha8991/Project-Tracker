# pages/projects.py
import streamlit as st
from components.project_form import render_project_form
from database import Database

def render_projects_page():
    st.title("Projects")
    
    db = Database()
    
    # Add new project section
    st.header("Add New Project")
    project_data = render_project_form()
    if project_data:
        db.add_project(**project_data)
        st.success("Project created successfully!")
        st.experimental_rerun()
    
    # List projects
    st.header("Project List")
    projects = db.get_projects()
    
    for project in projects:
        with st.expander(f"{project['name']} - {project['status']}"):
            st.write(f"Description: {project['description']}")
            st.write(f"Created: {project['created_at']}")
            
            if st.button(f"View Tasks", key=f"view_tasks_{project['id']}"):
                st.session_state.current_project = project['id']
                st.experimental_rerun()
                
render_projects_page()