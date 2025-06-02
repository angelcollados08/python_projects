from tkinter import *
#import playground

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

#LABEL
my_label = Label(text="I am a label", font=("Arial",24,"bold"))
#my_label.pack()
#my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)

my_label.config(text = "New text", padx=50,pady=50)



#Button
button = Button(text="Click me", command=button_clicked)
button2 = Button(text="new button")

#button.pack()
button.grid(column=1,row=1)
button2.grid(column=2,row=0)

#eNTRY

input = Entry(width=10)
#input.pack()
input.grid(column=3,row=2)



window.mainloop()