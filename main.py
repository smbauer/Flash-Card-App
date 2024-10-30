from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# set up UI
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# set up card images and text
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# add right and wrong buttons
x_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, borderwidth=0, relief="flat")
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, borderwidth=0, relief="flat")
right_button.grid(column=1, row=1)

window.mainloop()
