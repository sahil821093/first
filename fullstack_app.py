import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ================= 1. BACKEND =================
def setup_db():
    conn = sqlite3.connect("iibm_fullstack.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name TEXT, course TEXT, year TEXT)''')
    conn.commit()
    conn.close()

# ================= 2. FRONTEND LOGIC =================
def add_record():
    name = entry_name.get()
    course = entry_course.get()
    year = entry_year.get()

    if name == "" or course == "" or year == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("iibm_fullstack.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, course, year) VALUES (?, ?, ?)", (name, course, year))
    conn.commit()
    conn.close()

    clear_form()
    load_data() 
    messagebox.showinfo("Success", f"Record for {name} saved successfully!")

def delete_record():
    selected_item = tree.selection() # Get the clicked row
    if not selected_item:
        messagebox.showerror("Error", "Please select a record from the table to delete!")
        return
    
    # Extract the ID from the selected row
    item = tree.item(selected_item)
    record_id = item['values'][0]
    
    # Delete from database securely
    conn = sqlite3.connect("iibm_fullstack.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (record_id,))
    conn.commit()
    conn.close()
    
    load_data() # Refresh table
    messagebox.showinfo("Deleted", "Record deleted permanently!")

def load_data():
    for row in tree.get_children():
        tree.delete(row)
        
    conn = sqlite3.connect("iibm_fullstack.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    
    for record in records:
        tree.insert("", tk.END, values=record)
    conn.close()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_year.delete(0, tk.END)

# ================= 3. FRONTEND UI =================
setup_db() 

root = tk.Tk()
root.title("IIBM Full-Stack Manager Pro")
root.geometry("500x550")
root.config(bg="#1e1e2f")

tk.Label(root, text="Smart Student Database", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="#00ffcc").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Label(frame, text="Full Name:", bg="#1e1e2f", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame, font=("Arial", 12))
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Course:", bg="#1e1e2f", fg="white", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
entry_course = tk.Entry(frame, font=("Arial", 12))
entry_course.grid(row=1, column=1)

tk.Label(frame, text="Year:", bg="#1e1e2f", fg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
entry_year = tk.Entry(frame, font=("Arial", 12))
entry_year.grid(row=2, column=1)

# Action Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Save Record", font=("Arial", 12, "bold"), bg="#00ffcc", fg="black", command=add_record, width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Delete Selected", font=("Arial", 12, "bold"), bg="#ff4c4c", fg="white", command=delete_record, width=15).grid(row=0, column=1, padx=10)

# Data Table
columns = ("ID", "Name", "Course", "Year")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor=tk.CENTER)

tree.pack(pady=10, fill=tk.X, padx=20)

load_data()
root.mainloop()
