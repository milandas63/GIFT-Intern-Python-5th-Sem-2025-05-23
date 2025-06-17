import tkinter as tk

def new_file():
    print("New File")

def open_file():
    print("Open File")

def save_file():
    print("Save File")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Menu Example")
root.geometry("800x450")

# Create the menu bar
menu_bar = tk.Menu(root)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Configure the window to display the menu
root.config(menu=menu_bar)

root.mainloop()
