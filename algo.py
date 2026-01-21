import tkinter as tk

# Define all functions BEFORE calling them
def add_task():
    if inp.get():  # Get value from input widget
        db.add(inp.get())
        inp.delete(0, tk.END)  # Clear input field
        view_tasks()

def del_task():
    if inp.get():
        db.discard(inp.get())  # Use discard to avoid KeyError
        inp.delete(0, tk.END)
        view_tasks()

def view_tasks():
    task_list.delete(0, tk.END)
    for task in db:
        task_list.insert(tk.END, task)

def button_clicked():
    print("Button clicked!")

# Initialize data
db = {"task1", "task2"}
root = tk.Tk()
root.title("To-Do List")

# Create GUI elements
inp = tk.Entry(root, width=30)
inp.pack(pady=5)

# Buttons call the functions (without parentheses - just reference the function)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

del_button = tk.Button(root, text="Delete Task", command=del_task)
del_button.pack(pady=5)

task_list = tk.Listbox(root)
task_list.pack(pady=5)

view_tasks()  # Display initial tasks
root.mainloop()