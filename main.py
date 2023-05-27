from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    # resets timer and card doesn't flip automatically after 3 seconds.
    window.after_cancel(flip_timer)
    current_card = choice(data_dict)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg_image, image=front_photo)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(bg_image, image=back_photo)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    data_dict.remove(current_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")
bg_image = canvas.create_image(400, 263, image=front_photo)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
