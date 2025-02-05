import tkinter as tk
from tkinter import ttk
import database

def main():
    database.create_tasks_table()
    root = tk.Tk()
    root.title("Basic Task Tracker")

    # --- Explicitly Set Theme ---
    root.tk.call("lappend", "auto_path", "clam") # Add clam theme to auto_path (for some Tk versions)
    ttk.Style().theme_use('clam') # Set the theme to 'clam'

    style = ttk.Style()

    bg_color = "#1E293B"
    fg_color = "#F0F9FF"
    accent_color = "#7B00FF"
    button_bg = "#2D3748"
    button_fg = fg_color
    button_active_bg = accent_color

    style.configure("DarkFrame.TFrame", background=bg_color)


    style.configure("My.TButton", background="lightblue") # Just background color

    style.map("My.TButton", 
              background=[("active", button_active_bg),("!disabled", button_bg)],
              foreground=[("active", button_fg), ("!disabled", button_fg)]
              )
    
    root.configure(bg=bg_color)

    def load_tasks(): # Function to load tasks from DB - DEFINE FUNCTIONS *FIRST*
        tasks = database.get_tasks_from_db()
        for task in tasks:
            task_listbox.insert(tk.END, task['description'])

    def add_task(): # Function definition for add_task - DEFINE FUNCTIONS *FIRST*
        task_text = task_entry.get()
        if task_text:
            database.add_task_to_db(task_text)
            task_listbox.insert(tk.END, task_text)
            task_entry.delete(0, tk.END)

    def delete_task(): # Function definition for delete_task - DEFINE FUNCTIONS *FIRST*
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task_tuple_index = selected_task_index[0]
            selected_task_text = task_listbox.get(task_tuple_index)
            task_id_to_delete = None
            for task in database.get_tasks_from_db():
                if task['description'] == selected_task_text:
                    task_id_to_delete = task['id']
                    break
            if task_id_to_delete:
                database.delete_task_from_db(task_id_to_delete)
                task_listbox.delete(selected_task_index)


    
    # Task Listbox (UI element) - UI ELEMENT CREATION *AFTER* function definitions
    input_frame = ttk.Frame(root, style="DarkFrame.TFrame")
    input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # Task Entry Label
    task_label = ttk.Label(input_frame, text="Enter Task:", foreground=fg_color, background=bg_color)
    task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Task Input Entry
    task_entry = ttk.Entry(input_frame, width=40)
    task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Add Task Button
    add_button = ttk.Button(input_frame, text="Add Task", command=add_task, style="My.TButton")
    add_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    print(f"Add Button Style: {add_button.cget('style')}")

    # List Frame - Container for list and delete button
    list_frame = ttk.Frame(root, style="DarkFrame.TFrame")
    list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Task List Label
    list_label =ttk.Label(list_frame, text="Task List:", foreground=fg_color, background=bg_color)
    list_label.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
    
    # Task Listbox
    task_listbox = tk.Listbox(list_frame, height=10, width=50, bg=bg_color, fg=fg_color, selectbackground=accent_color, selectforeground=fg_color)
    task_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    # Delete Task Button
    delete_button = ttk.Button(list_frame, text="Delete Task", command=delete_task, style="My.TButton")
    delete_button.grid(row=2, column=0, padx=5, pady=5, sticky="se")
    print(f"Delete Button Style: {delete_button.cget('style')}")

    #configure grid column/row weights for resizing
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    list_frame.columnconfigure(0, weight=1)
    list_frame.rowconfigure(1, weight=1)

    load_tasks()

    root.mainloop()

if __name__ == "__main__":
    main()