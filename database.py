# database.py
import supabase
import streamlit as st
from config import SUPABASE_URL, SUPABASE_KEY
import httpx

class Database:
    def __init__(self):
        if not SUPABASE_URL or not SUPABASE_KEY:
            st.error("Supabase credentials are not configured. Please check your .env file.")
            # st.stop()
        try:
            self.client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)
            self.test_connection()
        except Exception as e:
            st.error(f"Failed to initialize Supabase client: {str(e)}")
            # st.stop()

    def test_connection(self):
        try:
            # Try to make a simple query to test the connection
            self.client.table('projects').select('count', count='exact').execute()
        except httpx.ConnectError:
            st.error("Unable to connect to Supabase. Please check your internet connection and Supabase URL.")
            # st.stop()
        except Exception as e:
            st.error(f"Connection test failed: {str(e)}")
            # st.stop()

    def get_projects(self):
        try:
            response = self.client.table('projects').select('*').execute()
            return response.data
        except Exception as e:
            st.error(f"Error fetching projects: {str(e)}")
            return []

    def add_project(self, name, description, status):
        try:
            data = {
                'name': name,
                'description': description,
                'status': status
            }
            return self.client.table('projects').insert(data).execute()
        except Exception as e:
            st.error(f"Error adding project: {str(e)}")
            return None

    def update_project(self, project_id, data):
        try:
            return self.client.table('projects').update(data).eq('id', project_id).execute()
        except Exception as e:
            st.error(f"Error updating project: {str(e)}")
            return None
        
    def update_task_status(self, task_id, new_status):
        try:
            result = self.client.table('tasks').update({"status": new_status}).eq('id', task_id).execute()
            return result.data
        except Exception as e:
            st.error(f"Error updating task status: {str(e)}")
            return None
        
    def update_project_status(self, project_id, new_status):
        try:
            result = self.client.table('projects').update({"status": new_status}).eq('id', project_id).execute()
            return result.data
        except Exception as e:
            st.error(f"Error updating project status: {str(e)}")
            return None

    def get_tasks(self, project_id=None):
        try:
            query = self.client.table('tasks').select('*')
            if project_id:
                query = query.eq('project_id', project_id)
            return query.execute().data
        except Exception as e:
            st.error(f"Error fetching tasks: {str(e)}")
            return []

    def add_task(self, project_id, title, description, assignee, status):
        try:
            data = {
                'project_id': project_id,
                'title': title,
                'description': description,
                'assignee': assignee,
                'status': status
            }
            return self.client.table('tasks').insert(data).execute()
        except Exception as e:
            st.error(f"Error adding task: {str(e)}")
            return None
