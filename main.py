import tkinter as tk
from tkinter import ttk
import os


window = tk.Tk()

window.title("Student Study Planner")
window.configure(bg="#F3F0F7")

# Title
title_label = tk.Label(window, text="Student Study Planner", font=("Arial", 20), bg="#F3F0F7", fg="#4B3F5C")
title_label.pack()

# Course selection
course_label = tk.Label(window, text="Course:", bg="#DCE6F1", fg="#4B5563")
course_label.pack()

course_box = ttk.Combobox(window)
course_box["values"] = ["CSC 240", "CSC 301", "CAL 151", "Other"]
course_box.pack()

# Task input
task_entry = tk.Entry(window, bg="#FFFFFF", fg="#40364D")
task_entry.pack()

# Task list
task_list = tk.Listbox(window, width=50, height=25, bg="#FFFFFF", fg="#40364D")
task_list.pack()


# Add a task
def add_task():
    task = task_entry.get()
    course = course_box.get()

    task_list.insert(tk.END, course + ": " + task)


# Remove a task
def remove_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task)


# Complete a task
def complete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task = task_list.get(selected_task)

        task_list.delete(selected_task)

        task_list.insert(
            selected_task,
            "✓ " + task
        )


# Save tasks
def save_tasks():
    file_path = os.path.join(os.path.dirname(__file__),"tasks.txt")

    with open(file_path, "w") as file:
        for task in task_list.get(0, tk.END):
            file.write(task + "\n")


# Load tasks
def load_tasks():
    file_path = os.path.join(os.path.dirname(__file__),"tasks.txt")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for task in file:
                task = task.strip()

                if task:
                    task_list.insert(tk.END, task)


# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(window,text="Remove Task",command=remove_task)
remove_button.pack()

complete_button = tk.Button(window,text="Complete Task",command=complete_task)
complete_button.pack()

save_button = tk.Button(window, text="Save Tasks",command=save_tasks)
save_button.pack()


# Load saved tasks when program starts
load_tasks()

window.mainloop()