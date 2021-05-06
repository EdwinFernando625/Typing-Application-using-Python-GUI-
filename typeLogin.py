import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

class MainLogin:
    name=""
    def Validate(self):
        MainLogin.name=user.get()
        if len(MainLogin.name)==0 or MainLogin.name[0]==' ':
            messagebox.showerror('Verifying','Please enter a valid username to continue')
        else:
            messagebox.showinfo('Verifying','Login success!')
            login.destroy()
ml=MainLogin()



login=tkinter.Tk()
login.geometry('400x200')
login.title('Typing Master login window')
login.resizable(0,0)

image2=Image.open("type1.jpg")
image1=ImageTk.PhotoImage(image2)
photo=Label(login,image=image1)
photo.pack()

user=StringVar()
user_label=Label(login,text='Username:  ',font=("Times New Roman",15),)
user_label.place(x=10,y=10)
user_entry=Entry(login,font=("Times New Roman",15),textvariable=user)
user_entry.place(x=220,y=25,anchor='center')

Enter=Button(login,text='Enter typing Master',font=("Arial",13),activebackground='green',bg='blue',bd='2px',padx=3,pady=3,command=ml.Validate)
Enter.place(x=160,y=90,anchor='center')

login.mainloop()