import tkinter
import typeLogin
from typeLogin import MainLogin
import random
import timeit 
import math
from PIL import ImageTk,Image
from timeit import default_timer as timer
from tkinter import*
from tkinter import messagebox
import fuzzywuzzy
from fuzzywuzzy import fuzz

def randomGenerator():
    var=(random.randint(1,30))
    print(var)
    file="Files//" + str(var) + ".txt"
    f=open(file,'r')
    content=str(f.readlines())
    content=content.strip('[\']')
    print(content)
    return content

if(MainLogin.name==""):
    name="Welcome Guest"
else:
    name="Welcome " +str(MainLogin.name)

class Time:
    startTime=float(0)
    endTime=float(0)
    similarity=float(0)
    speed=float(0)
    def startNow(self):
        display_entry.configure(state='normal')
        display_entry.focus()
        Time.startTime=timer()
        start.configure(state='disable')

    def stopNow(self,*args):
        display_entry.configure(state='disable')
        if Time.startTime!=0:
            start.configure(state='disable')
            Time.endTime=math.ceil(timer()-Time.startTime)
            print(("The total time is " +str(Time.endTime)))
            print(display_label['text'])
            Time.similarity=math.ceil(fuzz.ratio(display_label.cget("text"),result.get()))
            Time.speed=math.ceil(len(result.get())/(5*Time.endTime/60))
            print("The accuracy is: " +str(Time.similarity)+ "%")
            endResult['text']="Accuracy: " +str(Time.similarity)+ "%\nSpeed: " +str(Time.speed)+ " wpm\nTime taken: " +str(Time.endTime)+ " seconds" 
            stop.configure(state='disable')
        else:
            messagebox.showwarning('Warning','Please start the application before stopping')

t=Time()

def reset():
    display_label['text']=randomGenerator()
    display_entry.configure(state='normal')
    display_entry.delete(0,END)
    display_entry.configure(state='disable')
    start.configure(state='normal')
    stop.configure(state='normal')
    Time.startTime=0
    Time.endTime=0
    endResult['text']=""

main=tkinter.Tk()
main.title('Typing Master')
main.geometry('880x620')
main.resizable(0,0)
main.configure(bg='purple')

'''image4=ImageTk.Image.open("C:\\Users\\SelvanEdwin2\\Downloads\\type2.jpg")
image3=ImageTk.PhotoImage(image4)
photo=Label(main,image=image3)
photo.pack()'''

#welcome text
name_label=Label(main,text=name,font=("Times New Roman bold",20),bg='purple')
name_label.place(x=50,y=40)

read=Label(main,text="Type the highlighted text",font=("Times New Roman",15),bg='purple')
read.place(x=50,y=90)

#displays the text to be typed
display=StringVar()
display_label=Label(main,text=randomGenerator(),font=("Times New Roman",15),borderwidth=5,relief='ridge',bg='yellow',highlightcolor='black')
display_label.place(x=50,y=120)
read=Label(main,text="Type here:",font=("Times New Roman",15),bg='purple')
read.place(x=50,y=180)

#entry box to accept the text
result=StringVar()
display_entry=Entry(main,font=("Times New Roman",15),textvariable=result,state='disabled')
display_entry.bind('<Return>',t.stopNow)
display_entry.place(x=50,y=210,width=740)

start=Button(main,bg='green',text='Start',font=("Times New Roman",15),activebackground='blue',bd='3',command=t.startNow)
start.place(x=70,y=270)

stop=Button(main,bg='red',text='Stop',font=("Times New Roman",15),activebackground='blue',bd='3',command=t.stopNow)
stop.place(x=140,y=270)

reset=Button(main,bg='orange',text='Reset',font=("Times New Roman",15),activebackground='blue',bd='3',command=reset)
reset.place(x=210,y=270)

exit=Button(main,bg='black',fg='white',text='Exit',font=("Times New Roman",15),activebackground='blue',bd='3',command=main.destroy)
exit.place(x=290,y=270)

text=Label(main,text="Result: ",font=("Times New Roman bold",20),bg='purple')
text.place(x=50,y=330,height=80)

endResult=Label(main,text="",font=("Times New Roman",17,),bg='purple')
endResult.place(x=50,y=380,height=80)

main.mainloop()