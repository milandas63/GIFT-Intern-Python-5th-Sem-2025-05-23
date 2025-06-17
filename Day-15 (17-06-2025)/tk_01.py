import tkinter as tk

def newFile():
    return

root = tk.Tk()
root.title('My First Python Program')
root.iconbitmap('cup.png')
root.geometry('800x500')

mbar = tk.Menu(root)

mnuNew = tk.Menu(mbar, tearoff='0')
mnuNew.add_command(label='New', command=newFile)
mbar.add_cascade(label="File", menu=mnuNew)

greet = tk.Label(root, text='Hello World!', fg='blue', bg='lightgray', height='4', font=('Arial',28), border='25')
greet.pack()

name = tk.Entry(root, font=('Times Roman', 15))
name.pack()

address = tk.Text(root, height='5', font=('Times Roman',15))
address.pack()

resp = tk.Button(root, text=' Submit ', bg='blue', fg='yellow', font=('Arial', 20))
resp.pack()

root.mainloop()
