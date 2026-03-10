import sqlite3

def setup_database():
    # Initialize the connection to the SQLite database
    connection = sqlite3.connect("iibm_students.db")
    cursor = connection.cursor()
    
    # Create a structured table for student records
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            course TEXT NOT NULL,
            enrollment_year INTEGER
        )
    ''')
    connection.commit()
    return connection, cursor

def add_student(cursor, connection):
    print("\n--- 📝 New Student Registration ---")
    name = input("Enter Full Name: ")
    course = input("Enter Course (e.g., BCA): ")
    year = input("Enter Enrollment Year (e.g., 2026): ")
    
    # Insert data securely using parameterized queries
    cursor.execute('INSERT INTO students (full_name, course, enrollment_year) VALUES (?, ?, ?)', (name, course, int(year)))
    connection.commit()
    print(f"✅ Success: '{name}' has been successfully added to the IIBM Database.")

def view_all_students(cursor):
    print("\n--- 🗄️ IIBM Patna Official Student Records ---")
    cursor.execute('SELECT * FROM students')
    records = cursor.fetchall()
    
    if not records:
        print("⚠️ No records currently exist in the database.")
    else:
        print(f"{'ID':<5} | {'Full Name':<15} | {'Course':<10} | {'Year'}")
        print("-" * 50)
        for row in records:
            print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<10} | {row[3]}")
    print("-" * 50)

def delete_student(cursor, connection):
    print("\n--- 🗑️ Delete Student Record ---")
    student_id = input("Enter the ID of the student to remove: ")
    
    # Delete specific record based on the unique student ID
    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    connection.commit()
    print(f"✅ Success: Record with ID {student_id} has been permanently deleted.")

def main():
    conn, cursor = setup_database()
    
    while True:
        print("\n🏛️ Enterprise Database Portal (SQLite)")
        print("1. Add New Student")
        print("2. View All Records")
        print("3. Delete a Record")
        print("4. Exit System")
        choice = input("Select Option (1-4): ")

        if choice == '1':
            add_student(cursor, conn)
        elif choice == '2':
            view_all_students(cursor)
        elif choice == '3':
            delete_student(cursor, conn)
        elif choice == '4':
            conn.close()
            print("👋 System Closed. Database connection secured.")
            break
        else:
            print("❌ Invalid input. Please select a valid option.")

if __name__ == "__main__":
    main()
