"""
Project: Smart Task Manager (With Save Feature)
Author: Md Sahil
Description: A Python program that saves tasks to a file so data is never lost.
"""

import os
import datetime

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- 🚀 Sahil's Professional Task Manager ---")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def main():
    tasks = load_tasks()
    print(f"📂 Loaded {len(tasks)} tasks from memory.")
    
    while True:
        show_menu()
        choice = input("👉 Enter your choice (1-4): ")

        if choice == '1':
            task_text = input("Enter task details: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            full_task = f"[{timestamp}] {task_text}"
            tasks.append(full_task)
            save_tasks(tasks)
            print("✅ Task Saved Successfully!")

        elif choice == '2':
            print("\n📋 Your To-Do List:")
            if not tasks:
                print("   (List is empty. Add something!)")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"   {index}. {task}")

        elif choice == '3':
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: {removed}")
                else:
                    print("⚠️ Invalid number!")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '4':
            print("👋 Exiting... Your tasks are safe!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
    
