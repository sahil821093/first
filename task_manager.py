"""
Project: Smart Task Manager (With Priority Support)
Author: Md Sahil
Description: A Python program that saves tasks and their priority levels.
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
    print("\n--- 🚀 Sahil's Pro Task Manager ---")
    print("1. Add a New Task (with Priority)")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def main():
    tasks = load_tasks()
    print(f"📂 Loaded {len(tasks)} tasks.")
    
    while True:
        show_menu()
        choice = input("👉 Choice (1-4): ")

        if choice == '1':
            task_text = input("Enter task: ")
            print("Set Priority: [H] High, [M] Medium, [L] Low")
            p_input = input("Priority: ").upper()
            
            # Priority logic
            if p_input == 'H': priority = "🔴 HIGH"
            elif p_input == 'M': priority = "🟡 MED"
            else: priority = "🟢 LOW"

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            full_task = f"{priority} | {task_text} ({timestamp})"
            
            tasks.append(full_task)
            save_tasks(tasks)
            print("✅ Task Saved with Priority!")

        elif choice == '2':
            print("\n📋 Your Pro To-Do List:")
            if not tasks:
                print("   (List is empty)")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"   {index}. {task}")

        elif choice == '3':
            try:
                task_num = int(input("Task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: {removed}")
                else:
                    print("⚠️ Invalid number!")
            except ValueError:
                print("⚠️ Enter a valid number.")

        elif choice == '4':
            print("👋 Bye Sahil! Keep working hard.")
            break

if __name__ == "__main__":
    main()
    
