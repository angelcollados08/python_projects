BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

window = Tk()
window.title("flashy")
window.config(padx=100,pady=50, bg=BACKGROUND_COLOR, height=500, width=500)


file = pandas.read_csv("data/french_words.csv")
dict = file.to_dict(orient="records")
random_word = {}
def generate_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image = front_img)
    random_word = random.choice(dict) 
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    canvas.itemconfig(lenguage_text, text="French", fill = "black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global random_word
    canvas.itemconfig(canvas_image, image = back_img)
    canvas.itemconfig(word_text, text=random_word["English"] , fill = "white")
    canvas.itemconfig(lenguage_text, text="English", fill = "white")


flip_timer = window.after(3000, flip_card)
#Canvas

canvas = Canvas(width=800,height=526,bg = BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image =canvas.create_image(400,263,image=front_img)
lenguage_text = canvas.create_text(400,150,text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263,text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

button_right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=generate_word)
button_wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR,command=generate_word)
button_right.grid(row=1,column=1)
button_wrong.grid(row=1,column=0)
generate_word()




window.mainloop()