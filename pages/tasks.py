# pages/tasks.py
import streamlit as st
from components.task_form import render_task_form
from database import Database

def render_tasks_page(project_id):
    st.title("Tasks")
    
    db = Database()
    
    try:
        project = next((p for p in db.get_projects() if p['id'] == project_id), None)
        if not project:
            st.error("Project not found")
            return
    except Exception as e:
        st.error(f"Error loading project: {str(e)}")
        return
    
    st.header(f"Tasks for {project['name']}")
    
    # Add new task section
    with st.expander("Add New Task"):
        task_data = render_task_form(project_id)
        if task_data:
            db.add_task(**task_data)
            st.success("Task created successfully!")
            st.experimental_rerun()
    
    # List tasks
    tasks = db.get_tasks(project_id)
    status_options = ["Todo", "In Progress", "Review", "Done"]
    
    st.subheader("Task List")
    for task in tasks:
        with st.expander(f"{task['title']} - Current Status: {task['status']}", expanded=False):
            # Task Details
            st.write("### Task Details")
            st.write(f"**Description:** {task['description']}")
            st.write(f"**Assignee:** {task['assignee']}")
            st.write(f"**Created:** {task['created_at']}")
            
            # Status Update Section
            st.write("### Update Status")
            new_status = st.selectbox(
                "Select new status",
                status_options,
                index=status_options.index(task['status']),
                key=f"status_{task['id']}"
            )
            
            # Only show update button if status is different
            if new_status != task['status']:
                if st.button("Update Status", key=f"update_{task['id']}"):
                    db.update_task_status(task['id'], new_status)
                    st.success(f"Status updated to {new_status}!")
                    st.experimental_rerun()