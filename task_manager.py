"""
Project: Simple CLI Task Manager
Author: Md Sahil
Description: A Python program to manage daily tasks. 
It demonstrates the use of Lists, Loops, User Input, and Error Handling.
"""

import datetime  # Date aur time show karne ke liye

def show_menu():
    """User ke liye menu options print karta hai"""
    print("\n--- 🚀 My Task Manager (Built by Sahil) ---")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def main():
    tasks = []  # Empty list tasks store karne ke liye
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task details: ")
            # Professional touch: Task ke saath time bhi add kar rahe hain
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            tasks.append(f"[{now}] {task}")
            print(f"✅ Task Added Successfully!")

        elif choice == '2':
            print("\n📋 Your To-Do List:")
            if not tasks:
                print("   (No tasks found. Add some to get started!)")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"   {index}. {task}")

        elif choice == '3':
            # Error Handling: Agar user galat number daale toh crash nahi hoga
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ Deleted: {removed}")
                else:
                    print("⚠️ Invalid number! Please check the list again.")
            except ValueError:
                print("⚠️ Error: Please enter a valid number, not text!")

        elif choice == '4':
            print("👋 Exiting... Happy Coding!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Code yahan se shuru hoga
if __name__ == "__main__":
    main()
  
