from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="ChiQuiz")
    canvas.itemconfig(card_word, text =current_card["ChiQuiz"])


def flip_card():
    canvas.itemconfig(card_title, text="Answer", fill="white")
    canvas.itemconfig(card_word, text=current_card["Answer"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("ChiQuiz")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

canvas = Canvas(width= 800, height= 526)
card_front_img = PhotoImage(file="./images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 20, "bold"))
card_back_img = PhotoImage(file= "images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row= 0, column=0, columnspan = 2)

cross_image = PhotoImage(file="images/wrong.png")
unkown_button = Button(image=cross_image, highlightthickness= 0, command= flip_card)
unkown_button.grid(row=1, column=0, )

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness= 0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
