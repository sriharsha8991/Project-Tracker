# components/project_form.py
import streamlit as st

def render_project_form():
    with st.form("project_form"):
        name = st.text_input("Project Name")
        description = st.text_area("Description")
        status = st.selectbox("Status", ["Planning", "In Progress", "Completed", "On Hold"])
        
        submitted = st.form_submit_button("Create Project")
        if submitted:
            return {
                "name": name,
                "description": description,
                "status": status
            }
    return None