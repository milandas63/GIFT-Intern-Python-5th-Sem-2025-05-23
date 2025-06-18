from tkinter import *

root = Tk()
root.title("Login")

def retrieve():
    user = ent_username.get()
    word = ent_password.get()
    print("Username: ",user,", Password: ",word)
    lbl_result.config(text="Username: "+user+", Password: "+word)

lbl_caption = Label(root, text="L O G I N")
lbl_caption.grid(row=0, column=0, columnspan=3)

lbl_dummy1 = Label(root, text=" ")
lbl_dummy1.grid(row=1, column=0, columnspan=3)

lbl_username = Label(root, text="Username:")
lbl_username.grid(row=2, column=0)

ent_username = Entry(root, width=30)
ent_username.grid(row=3, column=0, columnspan=2)

lbl_dummy2 = Label(root, text=" ")
lbl_dummy2.grid(row=4, column=0, columnspan=3)

lbl_password = Label(root, text="Password:")
lbl_password.grid(row=5, column=0)

ent_password = Entry(root, width=30)
ent_password.grid(row=6, column=0, columnspan=3)

lbl_dummy3 = Label(root, text=" ")
lbl_dummy3.grid(row=7, column=0, columnspan=3)

lbl_dummy4 = Label(root, text=" ")
lbl_dummy4.grid(row=8, column=0, columnspan=3)

btn_submit = Button(root, text="Submit", padx="20", fg="blue", command=retrieve)
btn_submit.grid(row=9, column=1)

lbl_dummy5 = Label(root, text=" ")
lbl_dummy5.grid(row=10, column=0, columnspan=3)

lbl_result = Label(root, text=" ")
lbl_result.grid(row=11, column=0, columnspan=3)

root.mainloop()
