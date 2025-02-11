# pages/tasks.py
import streamlit as st
from components.task_form import render_task_form
from database import Database

def render_tasks_page(project_id):
    st.title("Tasks")
    
    db = Database()
    project = db.get_projects()[0]  # Get project details
    
    st.header(f"Tasks for {project['name']}")
    
    # Add new task section
    st.subheader("Add New Task")
    task_data = render_task_form(project_id)
    if task_data:
        db.add_task(**task_data)
        st.success("Task created successfully!")
        st.experimental_rerun()
    
    # List tasks
    st.subheader("Task List")
    tasks = db.get_tasks(project_id)
    
    for task in tasks:
        with st.expander(f"{task['title']} - {task['status']}"):
            st.write(f"Description: {task['description']}")
            st.write(f"Assignee: {task['assignee']}")
            st.write(f"Created: {task['created_at']}")
render_task_form(1)