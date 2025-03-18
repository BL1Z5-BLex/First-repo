import os
import json
import sys
from datetime import datetime 

Task_file = "Todo_list.json"

def load_task():
    if os.path.exists(Task_file):
        with open(Task_file , "r") as file:
            return json.load(file)

    return[]

def save_tasks(tasks):
    with open(Task_file, "w") as file:
        json.dump(tasks , file , indent=4)

def add_task(task):
    tasks = load_task()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print('Task added successfully')

def view_task(date_filter=None):
    tasks = load_task()
    filtered_task = []
    if date_filter:
        for task in tasks:
            task_date = datetime.strptime(task['timestamp'], "%Y-%m-%d %H:%M:%S").date()
            if task_date == date_filter:
                filtered_task.append(task)
    else:
        filtered_task = tasks 

    for i , task in enumerate(tasks , 1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}, {task['task']}, {status}")


def mark_as_done(task_number):
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True  
        save_tasks(tasks)
        print("Your task is marked as done.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nA Todo list made in python")
        print("1.Add task")
        print("2View task")
        print("3.Mark as done")
        print("4.Exit the todo list")
        choice = input("Please type in your choice:")



        if choice == '1':
            tasks = input("Enter the task: ")
            add_task(tasks)

        elif choice == '2':
            view_task()
    
        elif choice == '3':
            try:
           
                task_number = int(input("Please enter your task number:"))
                mark_as_done(task_number)

            except ValueError:
                print("Invalid number please try again:")

        elif choice == '4':
            print("Exiting the todo list.........")
            break
        
        else:
            print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    main()



    