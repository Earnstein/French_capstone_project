from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
words = {}

try:
    data = pandas.read_csv("C:/Users/HP/Desktop/python extract/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("C:/Users/HP/Desktop/python extract/data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words)
    french_word = current_word["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    english_word = current_word["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=card_back)


def known():
    words.remove(current_word)
    data = pandas.DataFrame(words)
    data.to_csv("C:/Users/HP/Desktop/python extract/data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 300, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Aerial", 40, "italic"))
card_word = canvas.create_text(400, 270, text="", font=("Aerial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="wrong.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="right.png")

right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)
next_word()

window.mainloop()
