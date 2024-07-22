from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fileds are Requierd')
    elif usernameEntry.get()=='priya' and passwordEntry.get()=='1234':
        messagebox.showinfo('success','login  is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong Credentials')
        
root=CTk()

root.geometry('930x478')
root.resizable(0,0)
# root.configure(fg_color='#161c30')
root.title('LOGIN PAGE')
image=CTkImage(Image.open('cover.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='EMPLOYEE MANAGEMENT SYSTEM',bg_color='#FFFFFF',font=('Goudy old style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20,y=100)


usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=100,y=200)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordEntry.place(x=100,y=250)

loginButton=CTkButton(root,text='LOGIN',cursor='hand2',command=login)
loginButton.place(x=120,y=300)

root.mainloop()

