import tkinter as tk 
from tkinter import messagebox
from datetime import datetime  
import os 
import json 


password = "12355"
Diary_file = "dairy1.json"

def check_password():
    if entry_pass.get() == password:
        login_window.withdraw()
        open_main_window()
    else:
        messagebox.showerror("Error" ,"Incorrect password please try again!")

def open_main_window():

    global main_window
    main_window = tk.Toplevel(login_window)
    main_window.title('Main Menu')
    main_window.geometry('400x350')

    wlc_lbl = tk.Label(main_window, text="Welcome User to the main menu of my diary App ", font=("Bold", 13))
    wlc_lbl.pack(pady=10)
    
    Add_btn = tk.Button(main_window, text="Add New", command=save_check, padx=20 , pady=10, font=("Arial",11))
    Add_btn.pack(pady=8)

    view_button = tk.Button(main_window, text="View Entries", padx=20, pady=10, font=("Arial",11), command=view_entry)
    view_button.pack(pady=8)
    
    exit_btn = tk.Button(main_window, text="Exit", command=exit_app, padx=20, pady=10, font=("Arial", 11))
    exit_btn.pack(pady=8)

    

    main_window.wait_window()



def save_check():
    diary_entry_window = tk.Toplevel(main_window)
    diary_entry_window.title('Save your entry here')
    diary_entry_window.geometry("450x500")
    
    tk.Label(diary_entry_window, text="Write your entry here:", font=("Arial",11)).pack(pady=8)

    diary_text = tk.Text(diary_entry_window, width=60, height=20)
    diary_text.pack(pady=10)

    save_button = tk.Button(diary_entry_window, text="Save", command=lambda: save_diary_entry(diary_text, diary_entry_window), padx=10,pady=10, font=("Arial", 12))
    save_button.pack(pady=8)

    


def save_diary_entry(diary_text, diary_entry_window):
    entry_text = diary_text.get("1.0", tk.END).strip()
    if not entry_text:
        messagebox.showerror("Warning", "Please enter the diary entry as it cannot be empty")
        return 
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry_data = {"timestamp": current_time, "entry": entry_text}

    try:
        with open(Diary_file, "r") as file:
            diary_entries = json.load(file)
    
    except(FileNotFoundError, json.JSONDecodeError):
        diary_entries = []

    diary_entries.append(entry_data)

    with open(Diary_file, "w") as file:
        json.dump(diary_entries, file, indent=4)



    messagebox.showinfo("SUCCESS", "Your diary is saved successfully")
    diary_entry_window.destroy()
    

def view_entry():
    try:
        with open(Diary_file, "r") as file:
            diary_entries = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Error", "NO entries are found")
        return
    
    if not diary_entries:
        messagebox.showinfo("INFO", "No entries ")
    
    
    entry_window = tk.Toplevel(main_window)
    entry_window.title("Written Diary Entries")
    entry_window.geometry("500x500")

    text_widget = tk.Text(entry_window, wrap="word", font=("Arail",12))
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    for entry in diary_entries:
        timestamp = entry.get("timestamp", "Unknown date")
        content = entry.get("entry", "No content")

        text_widget.insert(tk.END, f"{timestamp}\n", "bold")
        text_widget.insert(tk.END, f"{content}\n\n", "normal")


    text_widget.tag_config("bold", font=("Arial",12 ,"bold"))
    text_widget.config(state="disabled")

def exit_app():
    
    login_window.destroy()
    exit()




login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x250")

enter_pass = tk.Label(login_window, text="ENTER PASSWORD:" ,font=("Arial",10))
enter_pass.pack(pady=5)

entry_pass = tk.Entry(login_window, width = 15,show="*")
entry_pass.pack(pady=5)

login_btn = tk.Button(login_window,text="Login", command=check_password)
login_btn.pack(pady=5)





login_window.mainloop()