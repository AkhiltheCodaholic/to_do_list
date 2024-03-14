import tkinter as tk
from tkinter import messagebox

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if tasks:
        messagebox.showinfo("To-Do List", "\n".join(tasks))
    else:
        messagebox.showinfo("To-Do List", "No tasks found.")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    messagebox.showinfo("To-Do List", f"Task '{new_task}' added successfully.")

def mark_done(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] += " [Done]"
        save_tasks(tasks)
        messagebox.showinfo("To-Do List", f"Task {task_index} marked as done.")
    else:
        messagebox.showwarning("Invalid Task Index", "Invalid task index.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        messagebox.showinfo("To-Do List", f"Task {task_index} ('{removed_task}') removed.")
    else:
        messagebox.showwarning("Invalid Task Index", "Invalid task index.")

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = load_tasks()

        # Task entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.tasks_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.view_button = tk.Button(root, text="View Tasks", command=lambda: view_tasks(self.tasks))
        self.view_button.grid(row=1, column=1, padx=5, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=lambda: self.remove_task())
        self.remove_button.grid(row=2, column=1, padx=5, pady=10)

        self.mark_done_button = tk.Button(root, text="Mark as Done", command=lambda: self.mark_done())
        self.mark_done_button.grid(row=3, column=1, padx=5, pady=10)

        # Initialize the listbox with existing tasks
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            add_task(self.tasks, new_task)
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            remove_task(self.tasks, selected_task_index + 1)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")

    def mark_done(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            mark_done(self.tasks, selected_task_index + 1)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as done.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
