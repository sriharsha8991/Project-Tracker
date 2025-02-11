# components/project_form.py
import streamlit as st

def render_project_form():
    with st.form("project_form"):
        name = st.text_input("Project Name")
        description = st.text_area("Description")
        status = st.selectbox(
            "Status",
            ["Planning", "In Progress", "On Hold", "Completed"]
        )
        
        submitted = st.form_submit_button("Create Project")
        if submitted and name:  # Basic validation
            return {
                "name": name,
                "description": description,
                "status": status
            }
    return None