import streamlit as st

def render_task_status_update(current_status, on_update):
    status_options = ["Todo", "In Progress", "Review", "Done"]
    new_status = st.selectbox("Update Status", options=status_options, index=status_options.index(current_status))
    
    if new_status != current_status:
        if st.button(f"Update Status to {new_status}"):
            on_update(new_status)