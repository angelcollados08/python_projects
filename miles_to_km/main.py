from tkinter import *

window  = Tk()
window.title("Mile to Km Convert")
#window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

def button_clicked():
    new_text = int(input.get())
    my_label4.config(text=str(round(new_text*1.6)))

#LABELS
my_label1 = Label(text="Miles", font=("Arial",10,"bold"))
my_label2 = Label(text="Km", font=("Arial",10,"bold"))
my_label3 = Label(text="is equal to", font=("Arial",10,"bold"))
my_label4 = Label(text="0",font=("Arial",10,"bold"))
#my_label.pack()
#my_label.place(x=100,y=200)
my_label1.grid(column=2,row=0)
my_label2.grid(column=2,row=1)
my_label3.grid(column=0,row=1)
my_label4.grid(column=1,row=1)

#ENTRY

input = Entry(width=10)
#input.pack()
input.grid(column=1,row=0)

#BUTTON
button = Button(text="Calculate", command=button_clicked)

#button.pack()
button.grid(column=1,row=2)



window.mainloop()