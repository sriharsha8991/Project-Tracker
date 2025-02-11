import streamlit as st
from components.project_form import render_project_form
from database import Database

def render_projects_page():
    st.title("Projects")
    
    db = Database()
    
    # Add new project section
    with st.expander("Add New Project"):
        project_data = render_project_form()
        if project_data:
            db.add_project(**project_data)
            st.success("Project created successfully!")
            st.experimental_rerun()
    
    # List projects
    st.header("Project List")
    projects = db.get_projects()
    
    status_options = ["Planning", "In Progress", "On Hold", "Completed"]
    
    for project in projects:
        with st.expander(f"{project['name']} - Current Status: {project['status']}", expanded=False):
            # Project Details
            st.write("### Project Details")
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Created:** {project['created_at']}")
            
            # Status Update Section
            st.write("### Update Status")
            new_status = st.selectbox(
                "Select new status",
                status_options,
                index=status_options.index(project['status']),
                key=f"status_{project['id']}"
            )
            
            # Only show update button if status is different
            if new_status != project['status']:
                if st.button("Update Status", key=f"update_{project['id']}"):
                    db.update_project_status(project['id'], new_status)
                    st.success(f"Project status updated to {new_status}!")
                    st.experimental_rerun()
            
            # View Tasks Button
            if st.button("View Tasks", key=f"view_tasks_{project['id']}"):
                st.session_state.current_project = project['id']
                st.experimental_rerun()