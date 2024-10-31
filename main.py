from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Spanish"
STARTING_WORD = "Word"
FLIP_TIME = 5000

# import translations to dataframe
df = pd.read_csv("data/spanish_words.csv").to_dict(orient="records")


def choose_word():
    global english_word

    record = random.choice(df)
    spanish_word = record["Spanish"]
    english_word = record["English"]

    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text="Spanish", fill="black")
    canvas.itemconfig(word_text, text=spanish_word, fill="black")
    count_down()


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")


def count_down():
    window.after(FLIP_TIME, flip_card)


# set up UI
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# set up card images and text
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text=LANGUAGE, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text=STARTING_WORD, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# add right and wrong buttons
x_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, borderwidth=0, relief="flat", command=choose_word)
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, borderwidth=0, relief="flat", command=choose_word)
right_button.grid(column=1, row=1)

choose_word()

window.mainloop()
