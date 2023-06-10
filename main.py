from tkinter import *
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")

# ---------------------------- DRAW/FLIP FLASHCARD ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/polish.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}
learned = []


def i_know_it():
    to_learn.remove(current_card)
    df_to_learn = pandas.DataFrame(to_learn)
    df_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    draw_card()



def draw_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word = current_card["Polish"]
    canvas.itemconfig(vocab, text=word, fill="black")
    canvas.itemconfig(lang, text="Polish", fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back_photo)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(vocab, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_photo = PhotoImage(file='./images/card_front.png')
card_back_photo = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=card_photo)
lang = canvas.create_text(400, 150, text="Polish", font=FONT1, fill="black")
vocab = canvas.create_text(400, 263, text="word", font=FONT2, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(command=i_know_it, image=check_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
check_button.grid(row=1, column=0)

x_image = PhotoImage(file="./images/wrong.png")
x_button = Button(command=draw_card, image=x_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
x_button.grid(row=1, column=1)

draw_card()

window.mainloop()
