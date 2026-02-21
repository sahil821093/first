import os

# Filename to store data
DATA_FILE = "expenses.txt"

def add_expense():
    print("\n--- ➕ Add New Expense ---")
    item = input("Enter item/service name: ")
    amount = input("Enter amount (in INR): ")
    
    # Opening the file in 'append' mode so data isn't deleted
    with open(DATA_FILE, "a") as file:
        file.write(f"Item: {item} | Amount: ₹{amount}\n")
    print("✅ Expense saved successfully!")

def view_expenses():
    print("\n--- 📜 Your Expense History ---")
    # Checking if the file exists before reading
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No expenses recorded yet.")
    else:
        print("No data file found. Add an expense first.")

def main():
    while True:
        print("\n--- 💰 Sahil's Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting... Keep tracking your savings!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

