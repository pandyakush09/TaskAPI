import streamlit as st
import requests

# Set the base URL for the FastAPI backend
BASE_URL = "http://127.0.0.1:8000"

st.title("Task Management System")

# Tabs for User and Task management
tab1, tab2 = st.tabs(["Users", "Tasks"])

# USER MANAGEMENT
with tab1:
    st.header("User Management")

    # Create a new user
    st.subheader("Create User")
    user_name = st.text_input("Name")
    user_email = st.text_input("Email")
    user_password = st.text_input("Password", type="password")
    if st.button("Create User"):
        user_data = {"name": user_name, "email": user_email, "password": user_password}
        response = requests.post(f"{BASE_URL}/user/", json=user_data)
        if response.status_code == 201:
            st.success("User created successfully!")
        else:
            st.error(f"Error: {response.json().get('detail')}")

    # List all users
    st.subheader("List Users")
    if st.button("Fetch Users"):
        response = requests.get(f"{BASE_URL}/user/")
        if response.status_code == 200:
            users = response.json()
            for user in users:
                st.write(f"Name: {user['name']}, Email: {user['email']}")
        else:
            st.error("Error fetching users!")

# TASK MANAGEMENT
with tab2:
    st.header("Task Management")

    # Create a new task
    st.subheader("Create Task")
    task_title = st.text_input("Task Title")
    task_description = st.text_area("Task Description")
    task_completed = st.checkbox("Completed")
    if st.button("Create Task"):
        task_data = {"title": task_title, "description": task_description, "completed": task_completed}
        response = requests.post(f"{BASE_URL}/task/", json=task_data)
        if response.status_code == 201:
            st.success("Task created successfully!")
        else:
            st.error(f"Error: {response.json().get('detail')}")

    # List all tasks
    st.subheader("List Tasks")
    if st.button("Fetch Tasks"):
        response = requests.get(f"{BASE_URL}/task/")
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                st.write(f"Title: {task['title']}, Description: {task['description']}, Completed: {task['completed']}")
        else:
            st.error("Error fetching tasks!")

    # Update a task
    st.subheader("Update Task")
    update_task_id = st.text_input("Task ID to Update")
    update_task_title = st.text_input("Updated Title")
    update_task_description = st.text_area("Updated Description")
    update_task_completed = st.checkbox("Completed?")
    if st.button("Update Task"):
        update_data = {
            "title": update_task_title,
            "description": update_task_description,
            "completed": update_task_completed,
        }
        response = requests.put(f"{BASE_URL}/task/{update_task_id}", json=update_data)
        if response.status_code == 202:
            st.success("Task updated successfully!")
        else:
            st.error(f"Error: {response.json().get('detail')}")

    # Delete a task
    st.subheader("Delete Task")
    delete_task_id = st.text_input("Task ID to Delete")
    if st.button("Delete Task"):
        response = requests.delete(f"{BASE_URL}/task/{delete_task_id}")
        if response.status_code == 204:
            st.success("Task deleted successfully!")
        else:
            st.error(f"Error: {response.json().get('detail')}")
