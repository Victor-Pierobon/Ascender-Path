import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Basic Task Tracker")

    def add_task():  # Define the add_task function here
        task_text = task_entry.get()  # Get text from the Entry widget
        if task_text: # Check if the task_text is not empty
            task_listbox.insert(tk.END, task_text) # Insert task into Listbox
            task_entry.delete(0, tk.END) # Clear the Entry widget

    def delete_task():
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task_listbox.delete(selected_task_index)

    # Task Input Entry (UI element - remains the same)
    task_entry = ttk.Entry(root, width=40)
    task_entry.pack(pady=10)

    # Add Task Button (UI element - will be modified in next step)
    add_button = ttk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    # Delete Task Button 
    delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack(pady=5)

    # Task Listbox (UI element - remains the same)
    task_listbox = tk.Listbox(root, height=10, width=50)
    task_listbox.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()