#!/usr/bin/env python
# coding: utf-8

# In[58]:


import tkinter as tk
from tkinter import messagebox
import datetime
import os

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                task_info = line.strip().split('|')
                task = {
                    'task': task_info[0],
                    'priority': int(task_info[1]),
                    'completed': task_info[2] == 'True',
                    'due_date': datetime.datetime.strptime(task_info[3], '%Y-%m-%d').date() if task_info[3] else None,
                }
                tasks.append(task)
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            due_date_str = task['due_date'].strftime('%Y-%m-%d') if task['due_date'] else ''
            file.write(f"{task['task']}|{task['priority']}|{task['completed']}|{due_date_str}\n")

# Function to add a new task
def add_task():
    task_name = entry_task_name.get()
    priority = int(entry_priority.get())
    due_date_str = entry_due_date.get()
    if due_date_str:
        try:
            due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return
    else:
        due_date = None
    task = {
        'task': task_name,
        'priority': priority,
        'completed': False,
        'due_date': due_date,
    }
    tasks.append(task)
    save_tasks(tasks)
    display_tasks()

# Function to remove a task
def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        del tasks[selected_task_index]
        save_tasks(tasks)
        display_tasks()

# Function to mark a task as completed
def mark_task_completed():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        tasks[selected_task_index]['completed'] = True
        save_tasks(tasks)
        display_tasks()

# Function to display tasks with details
def display_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓" if task['completed'] else " "
        due_date = f" (Due: {task['due_date']})" if task['due_date'] else ""
        task_details = f"{i + 1}. [{status}] {task['task']} (Priority: {task['priority']}){due_date}"
        task_list.insert(tk.END, task_details)

# Create or load the tasks list
tasks = load_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("800x700")  # Set dimensions

# Customize the window background color
root.configure(bg="#AFFAF0")  # Specify your preferred color

# Entry fields with background color
label_task_name = tk.Label(root, text=" Task Name : ", bg="#FFFFE0",font=("Arial", 14))
label_task_name.pack(pady=1)

entry_task_name = tk.Entry(root,width=50, font=("Arial", 14))
entry_task_name.pack(pady=10)



label_priority = tk.Label(root, text="Priority (1-high , 2-medium, 3-low ):", bg="#FFFFE0",font=("Arial", 14))
label_priority.pack(pady=1)

entry_priority = tk.Entry(root,width=50, font=("Arial", 14))
entry_priority.pack(pady=10)

label_due_date = tk.Label(root, text="Due Date (YYYY-MM-DD, optional):", bg="#FFFFE0",font=("Arial", 14))
label_due_date.pack(pady=1)
entry_due_date = tk.Entry(root,width=50, font=("Arial", 14))
entry_due_date.pack(pady=10)

# Buttons with background colors
add_button = tk.Button(root,width=10,height=2, text="Add Task", command=add_task, bg="green", fg="white",font=("Arial", 10))
add_button.pack(pady=5)

remove_button = tk.Button(root,width=20,height=2, text="Remove Task", command=remove_task, bg="red", fg="white",font=("Arial", 10))
remove_button.pack(pady=5)

mark_completed_button = tk.Button(root,width=20,height=2, text="Mark as Completed", command=mark_task_completed, bg="blue", fg="white",font=("Arial", 10))
mark_completed_button.pack(pady=5)

# Task list with background color
task_list = tk.Listbox(root, width=50, height=50, bg="#FFFFE0",font=("Arial", 14))
task_list.pack(pady=10)

# Display existing tasks
display_tasks()

root.mainloop()


# In[ ]:





# In[8]:





# In[ ]:




