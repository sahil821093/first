import sqlite3

# Step 1: Connect to the database (It creates the file automatically if missing)
conn = sqlite3.connect("expenses_high_storage.db")
cursor = conn.cursor()

# Step 2: Create a structured table for high-capacity data storage
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        amount REAL NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

def add_expense():
    print("\n--- ➕ Add New Expense ---")
    item = input("Enter item/service name: ")
    try:
        amount = float(input("Enter amount (in INR): "))
        
        # Step 3: Securely insert data into the SQL database
        cursor.execute("INSERT INTO expenses (item_name, amount) VALUES (?, ?)", (item, amount))
        conn.commit()
        print("✅ Expense saved securely in the Database!")
    except ValueError:
        print("❌ Invalid amount. Please enter a numerical value.")

def view_expenses():
    print("\n--- 📜 Your Expense History (Database View) ---")
    
    # Step 4: Fetch data from the database
    cursor.execute("SELECT item_name, amount, date FROM expenses")
    records = cursor.fetchall()
    
    if records:
        # Formatting the output like a professional table
        print(f"{'Item':<15} | {'Amount':<10} | {'Date'}")
        print("-" * 45)
        for row in records:
            print(f"{row[0]:<15} | ₹{row[1]:<9} | {row[2][:10]}")
    else:
        print("ℹ️ No expenses recorded in the database yet.")

def main():
    while True:
        print("\n--- 💰 Advanced Expense Tracker (SQL Edition) ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting... Database connection closed safely.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    # Always close the connection to prevent data leaks
    conn.close()
  
