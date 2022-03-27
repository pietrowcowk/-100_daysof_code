import turtle
from matplotlib import image
import pandas as pd

screen = turtle.Screen()
screen.title = ('U.S. State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv('50_states.csv')
list_of_states = data.state.to_list()

guessed = []

while len(guessed) < 50:
    answer = screen.textinput(f'{len(guessed)}/50 States Correct', 'What\'s another state').title()

    if answer == 'Exit':
        missing_states = []
        missing_states = [state for state in list_of_states if state not in guessed]
        to_learn_labels = ['states_to_learn']
        to_learn = pd.DataFrame(missing_states, columns=to_learn_labels)
        to_learn.to_csv('States_to_learn.csv', index=False)
        break
        
    if answer in list_of_states:
        states_title = turtle.Turtle()
        states_title.hideturtle()
        states_title.penup()
        state_loc = data[data.state == answer]
        states_title.goto(int(state_loc.x), int(state_loc.y))
        states_title.write(answer)
        guessed.append(answer)

turtle.mainloop() # alternative to screen.exitonclick()
