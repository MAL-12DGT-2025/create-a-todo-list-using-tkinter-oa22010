import tkinter as tk
from tkinter import ttk

# Function to read and return text in file
def read_text(todo_text):
    with open(todo_text, 'r') as todo_file:
        tasks = todo_file.readlines()
        return [task.strip() for task in tasks]

root = tk.Tk()
root.title('Todo List')

# Load tasks from the file
tasks = read_text('todo.txt')

# Creates widgets
list_text = tk.Label(text='Todo List')
list_text.grid(row=0, column=0, columnspan=2)

checkbox_a = tk.Checkbutton(text='')
checkbox_a.grid(row=1, column=0)

checkbox_b = tk.Checkbutton(text='')
checkbox_b.grid(row=2, column=0)

checkbox_c = tk.Checkbutton(text='')
checkbox_c.grid(row=3, column=0)

checkbox_d = tk.Checkbutton(text='')
checkbox_d.grid(row=4, column=0)

checkbox_e = tk.Checkbutton(text='')
checkbox_e.grid(row=5, column=0)

checkbox_g = tk.Checkbutton(text='')
checkbox_g.grid(row=6, column=0)

checkbox_h = tk.Checkbutton(text='')
checkbox_h.grid(row=7, column=0)

label_a = ttk.Label(text=tasks[0] if len(tasks) > 0 else '')
label_a.grid(row=1, column=1, padx=5, pady=5)

label_b = ttk.Label(text=tasks[1] if len(tasks) > 1 else '')
label_b.grid(row=2, column=1, padx=5, pady=5)

label_c = ttk.Label(text=tasks[2] if len(tasks) > 2 else '')
label_c.grid(row=3, column=1, padx=5, pady=5)

label_d = ttk.Label(text=tasks[3] if len(tasks) > 3 else '')
label_d.grid(row=4, column=1, padx=5, pady=5)

label_e = ttk.Label(text=tasks[4] if len(tasks) > 4 else '')
label_e.grid(row=5, column=1, padx=5, pady=5)

label_f = ttk.Label(text=tasks[5] if len(tasks) > 5 else '')
label_f.grid(row=6, column=1, padx=5, pady=5)

label_g = ttk.Label(text=tasks[6] if len(tasks) > 6 else '')
label_g.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()