
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILE_NAME = "tasks.json"
tasks = []

# Load saved tasks
def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, OSError):
            tasks = []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Refresh task list
def refresh_tasks():
    task_list.delete(0, tk.END)

    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "○"
        task_list.insert(
            tk.END,
            f"{status}  {task['title']}"
        )

# Add task
def add_task():
    title = task_entry.get().strip()

    if not title:
        messagebox.showwarning("Warning", "Enter a task first!")
        return

    tasks.append({"title": title, "completed": False})
    task_entry.delete(0, tk.END)
    save_tasks()
    refresh_tasks()

# Delete task
def delete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    del tasks[selected[0]]
    save_tasks()
    refresh_tasks()

# Update task
def update_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    index = selected[0]
    new_title = simpledialog.askstring(
        "Update Task",
        "Enter the updated task:",
        initialvalue=tasks[index]["title"]
    )

    if new_title and new_title.strip():
        tasks[index]["title"] = new_title.strip()
        save_tasks()
        refresh_tasks()

# Mark task completed
def complete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    index = selected[0]
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks()
    refresh_tasks()

# Main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("650x650")
root.configure(bg="#F4F6F8")
root.resizable(False, False)

# Header
header = tk.Frame(root, bg="#263A53", height=120)
header.pack(fill="x")

tk.Label(
    header,
    text="MY TASK MANAGER",
    font=("Arial", 25, "bold"),
    bg="#263A53",
    fg="white"
).pack(pady=(25, 5))

tk.Label(
    header,
    text="Organize your day, one task at a time",
    font=("Arial", 11),
    bg="#263A53",
    fg="#D5DFE9"
).pack()

# Main content
main = tk.Frame(root, bg="#F4F6F8")
main.pack(fill="both", expand=True, padx=35, pady=25)

tk.Label(
    main,
    text="Add a New Task",
    font=("Arial", 15, "bold"),
    bg="#F4F6F8",
    fg="#263A53"
).pack(anchor="w", pady=(0, 10))

task_entry = tk.Entry(
    main,
    font=("Arial", 13),
    bd=1,
    relief="solid"
)
task_entry.pack(fill="x", ipady=12, pady=(0, 18))

add_button = tk.Button(
    main,
    text="+  ADD TASK",
    command=add_task,
    font=("Arial", 11, "bold"),
    bg="#20B477",
    fg="white",
    bd=0,
    cursor="hand2"
)
add_button.pack(fill="x", ipady=10, pady=(0, 22))

tk.Label(
    main,
    text="YOUR TASKS",
    font=("Arial", 15, "bold"),
    bg="#F4F6F8",
    fg="#263A53"
).pack(anchor="w", pady=(0, 10))

task_list = tk.Listbox(
    main,
    font=("Arial", 13),
    height=10,
    bd=0,
    relief="flat",
    selectbackground="#DCEFE7",
    selectforeground="#263A53",
    activestyle="none"
)
task_list.pack(fill="both", expand=True, pady=(0, 18))

# Action buttons
actions = tk.Frame(main, bg="#F4F6F8")
actions.pack(fill="x")

def make_button(parent, text, command, color):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg="white",
        font=("Arial", 10, "bold"),
        bd=0,
        cursor="hand2"
    )

make_button(actions, "✓ COMPLETE", complete_task, "#20B477").pack(
    side="left", expand=True, fill="x", padx=3, ipady=10
)

make_button(actions, "EDIT", update_task, "#527AA3").pack(
    side="left", expand=True, fill="x", padx=3, ipady=10
)

make_button(actions, "DELETE", delete_task, "#D65A5A").pack(
    side="left", expand=True, fill="x", padx=3, ipady=10
)

load_tasks()
refresh_tasks()

root.mainloop()
