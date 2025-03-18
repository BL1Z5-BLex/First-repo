from customtkinter import *
import os 
import json 
import sys
from datetime import datetime 
from PIL import Image
from tkinter import messagebox  # Import messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window = CTk()
window.geometry("500x500")

window.iconbitmap(resource_path('icon_app_new.ico'))

Task_file = resource_path("tasks.json")

set_appearance_mode("dark")

def load_tasks():
    try:
        with open(Task_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_task(tasks):
    with open(Task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    add_window = CTkToplevel(window)
    add_window.geometry("300x200")
    add_window.title("Add Task")

    add_window.lift()
    add_window.attributes("-topmost", True)

    task_label = CTkLabel(add_window, text="Enter Task:")
    task_label.pack(pady=5)

    task_entry = CTkEntry(add_window, width=250)
    task_entry.pack(pady=5)

    def save_new_task():
        task = task_entry.get().strip()  # Ensure no empty spaces
        if task:
            tasks = load_tasks()  # Load existing tasks
            tasks.append({"task": task, "done": False})  # Append new task
            save_task(tasks)  # Save back to file
            messagebox.showinfo("Success", "Your task has been saved successfully!")
            add_window.destroy()
        else:
            messagebox.showwarning("Warning", "Task Box cannot be empty!")

    save_btn = CTkButton(add_window, text="Save", command=save_new_task)
    save_btn.pack(pady=10)

def view_task():
    view_window = CTkToplevel(window)
    view_window.geometry("400x300")
    view_window.title("Saved Tasks")

    view_window.lift()
    view_window.attributes("-topmost", True)

    tasks = load_tasks()  # 🔵 RELOAD TASKS FROM FILE
    if not tasks:
        msg = CTkLabel(view_window, text="No available tasks")
        msg.pack(pady=20)
    else:
        for task in tasks:
            task_text = f"✔ {task['task']}" if task['done'] else f"❌ {task['task']}"
            task_label = CTkLabel(view_window, text=task_text)
            task_label.pack()

def mark_task_done():
    mark_window = CTkToplevel(window)
    mark_window.geometry("400x300")
    mark_window.title("Mark Tasks as Done")

    mark_window.lift()
    mark_window.attributes("-topmost", True)

    tasks = load_tasks()  # 🔵 LOAD TASKS AGAIN
    if not tasks:
        msg = CTkLabel(mark_window, text="No tasks available")
        msg.pack()
        return
    
    task_list = [task["task"] for task in tasks if not task["done"]]  # Only show pending tasks
    if not task_list:
        msg = CTkLabel(mark_window, text="All tasks are already completed!")
        msg.pack()
        return

    selected_task = CTkComboBox(mark_window, values=task_list)
    selected_task.pack(pady=10)

    def mark_done():
        selected = selected_task.get()
        for task in tasks:
            if task["task"] == selected:
                task["done"] = True  # Mark task as done
                break
        save_task(tasks)  # 🔵 SAVE CHANGES TO FILE
        messagebox.showinfo("Success", f"Task '{selected}' marked as done!")
        mark_window.destroy()

    done_btn = CTkButton(mark_window, text="Mark as Done", command=mark_done)
    done_btn.pack(pady=10)

# UI Buttons
wlc_text = CTkLabel(master=window, text="Welcome to the menu of your todo list", font=("Segoe UI Semibold", 20))
wlc_text.place(relx=0.5, rely=0.1, anchor="center")

add_btn = CTkButton(master=window, text="➕ Add Task", corner_radius=35, fg_color="#015BBB", hover_color="#B5201B", border_color="#FED700", border_width=3, command=add_task)
add_btn.place(relx=0.5, rely=0.25, anchor="center")

view_btn = CTkButton(master=window, text="👁 View Tasks", corner_radius=35, fg_color="#015BBB", hover_color="#B5201B", border_color="#FED700", border_width=3, command=view_task)
view_btn.place(relx=0.5, rely=0.35, anchor="center")

markas_done = CTkButton(master=window, text="✔ Mark as Done", corner_radius=35, fg_color="#015BBB", hover_color="#B5201B", border_color="#FED700", border_width=3, command=mark_task_done)
markas_done.place(relx=0.5, rely=0.45, anchor="center")

exit_btn = CTkButton(master=window, text="❌ Exit", corner_radius=35, fg_color="#015BBB", hover_color="#B5201B", border_color="#FED700", border_width=3, command=window.quit)
exit_btn.place(relx=0.5, rely=0.55, anchor="center")

window.mainloop()
