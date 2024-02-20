import tkinter as tk
from tkinter import *
import string
import random
import pyperclip

root = tk.Tk()
root.title("Password Generator")
root.geometry("700x500")
root.configure(bg="#C1CDCD")
passwrd = StringVar()
passlen = IntVar()


def generate_password():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    password =""
    for x in range(passlen.get()):
        password = password + random.choice(s)
        passwrd.set(password)

def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)

label = tk.Label(root, text="Password Generator", font=("Helvetica, 18"), bd=1, relief="solid", width = 100, bg="#EEB422")
label.pack(pady=20)

name = tk.Label(root, text="Enter User Name :" ,font=("Helvetica, 18"), bg="#C1CDCD")
name.place(x=20, y=80)

entry = tk.Entry(root, font=("Helvetica, 18") )
entry.place(x=250, y=80)

length = tk.Label(root, text="Set Password Length :" ,font=("Helvetica, 18"), bg="#C1CDCD")
length.place(x=20, y=150)

pwlength = tk.Entry(root, font=("Helvetica, 18"), textvariable=passlen)
pwlength.place(x=300, y=150)

generated_pass = tk.Label(root, text="Generated Password :" ,font=("italic, 18"),bg="#C1CDCD")
generated_pass.place(x=20, y=220)

btn_1 = tk.Button(root, text="Generate Password", font=("Helvetica, 18"), width=30, command=generate_password, activebackground='#78d6ff',bg="#FFF8DC")
btn_1.place(x=130, y=300)

genpasswrd = tk.Entry(root, font=("Helvetica, 18"), textvariable=passwrd )
genpasswrd.place(x=300, y=220)

btn_2 = tk.Button(root, text="Copy", font=("Helvetica, 18"),command=copyclipboard, activebackground="#78d6ff",bg="#FFF8DC")
btn_2.place(x=600, y=210)
root.mainloop()


































# import string
# import random
# if __name__ == '__main__':
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.digits
#     s4 = string.punctuation
#
#     plen = int(input("Enter the length of the password :\n"))
#
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#
#     random.shuffle(s)
#     print("".join(s[0:plen]))






