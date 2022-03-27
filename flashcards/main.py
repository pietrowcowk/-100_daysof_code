from tkinter import *
import pandas as pd
import random
import tkinter

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    french_words = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = french_words.to_dict(orient='records') #combine English word with French word

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) #stop counting if known_button or unknown_button was clicked and start countinf from 0
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_backgorund, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_backgorund, image=card_back_img)

def word_is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv')
    next_card()

window = Tk()
window.title('Flash Cards')
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file='./images/card_back.png')
card_front_img = PhotoImage(file='./images/card_front.png')
card_backgorund = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 100, text='French', font=('Arial', 40, 'normal'))
card_word = canvas.create_text(400, 250, text='', font=('Arial', 100, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file='./images/wrong.png')
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file='./images/right.png')
known_button = Button(image=right_image, highlightthickness=0, command=word_is_known)
known_button.grid(row=1, column=1)

next_card()

tkinter.mainloop()