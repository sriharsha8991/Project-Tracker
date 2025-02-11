# components/task_form.py
import streamlit as st

def render_task_form(project_id):
    with st.form("task_form"):
        title = st.text_input("Task Title")
        description = st.text_area("Task Description")
        assignee = st.text_input("Assignee")
        status = st.selectbox("Status", ["Todo", "In Progress", "Review", "Done"])
        
        submitted = st.form_submit_button("Create Task")
        if submitted:
            return {
                "project_id": project_id,
                "title": title,
                "description": description,
                "assignee": assignee,
                "status": status
            }
    return None