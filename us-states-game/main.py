import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("us-states-game/50_states.csv")
data_dict = data.set_index(data.columns[0]).apply(tuple,axis=1).to_dict()

while len(data_dict) != 0:
    answer_state = screen.textinput(title=f"{50-len(data_dict)}/50 Guess the State",prompt="What's another State's name?")
    if answer_state == "exit":
        fr = pandas.DataFrame(data_dict)
        fr.to_csv("us-states-game/remaining.csv")
        break
    answer_state = answer_state.capitalize()
    if answer_state in data_dict:
        writer.goto(data_dict[answer_state][0],data_dict[answer_state][1])
        del data_dict[answer_state]
        writer.write(answer_state)




