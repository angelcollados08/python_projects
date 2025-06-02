from tkinter import *
from tkinter import ttk
import random
import requests


root = Tk()
root.title("Typing speed game")

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

timer = 60
def timer_func():
    global timer
    timer -= 1
    label_timer_num.config(text=timer)
    label_timer_num.after(1000,timer_func)


correct_words = 0
wrong_words = 0
def calculate(*args):
    try:
        global correct_words
        global wrong_words
        global words
        words += 1
        label_words_num.config(text=words)
        if word_rand == name.get():
            correct_words += 1
        else:
            wrong_words +=1
        word_rand.set(random.choice(WORDS))
        name.delete(0,END)
        timer_func()
    except ValueError:
        pass



words = 0



s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
# ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()

mainframe = ttk.Frame(root, width=200, height=200,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
label = StringVar()
label = ttk.Label(mainframe, text='Welcome to typing speed game')
label.grid(column=1,row=0)

label_words = ttk.Label(mainframe, text='WORDS')
label_words.grid(column=0,row=1)

label_words_num = ttk.Label(mainframe, text=words)
label_words_num.grid(column=0,row=2)

image = PhotoImage(file='timer.png')
label_image = ttk.Label(mainframe,image=image)
label_image.grid(column=1,row=1)

label_timer = ttk.Label(mainframe, text='TIMER')
label_timer.grid(column=2,row=1)

label_timer_num = ttk.Label(mainframe, text=timer)
label_timer_num.grid(column=2,row=2)

word_rand = StringVar()
word_rand.set(random.choice(WORDS))
label_random_word= ttk.Label(mainframe, textvariable=word_rand)
label_random_word.grid(column=1,row=2)

username = StringVar()
name = ttk.Entry(mainframe, textvariable=username)
name.grid(column=1,row=3)

c_words = StringVar()
ttk.Label(mainframe, textvariable=c_words).grid(column=1, row=4, sticky=(W, E))
b_words = StringVar()
ttk.Label(mainframe, textvariable=b_words).grid(column=1, row=5, sticky=(W, E))

c_words_label = ttk.Label(mainframe, text='CORRECT WORDS')
c_words_label.grid(column=0, row=4, sticky=(W, E))
b_words_label = ttk.Label(mainframe, text='BAD WORDS')
b_words_label.grid(column=0, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)



name.focus()
root.bind("<Return>", calculate)

root.mainloop()