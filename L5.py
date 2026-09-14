import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("400x400")


# Add a task
def add_task():
    task = entry.get()

    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


# Delete selected task
def delete_task():
    selected = listbox.curselection()

    if selected:
        listbox.delete(selected[0])


# Title
title = tk.Label(
    window,
    text="My To-Do List",
    font=("Arial", 20)
)
title.pack(pady=10)


# Input box
entry = tk.Entry(
    window,
    width=30
)
entry.pack(pady=10)


# Add button
add_button = tk.Button(
    window,
    text="Add Task",
    command=add_task
)
add_button.pack(pady=5)


# List of tasks
listbox = tk.Listbox(
    window,
    width=40,
    height=12
)
listbox.pack(pady=10)


# Delete button
delete_button = tk.Button(
    window,
    text="Delete Task",
    command=delete_task
)
delete_button.pack(pady=5)


# Start the application
window.mainloop()
