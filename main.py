import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
#You need to add the image with a method from the class screen, to be able to use as a turtle shape.
screen.addshape(image)

turtle.shape(image)
#You read the csv file and assign it to a variable.
data = pandas.read_csv("50_states.csv")
#Turn a column to a list. "state" is a column on the csv file.
all_states = data.state.to_list()
#You are accessing a column, but you still need to convert it to a list.
all_x = data.x.to_list()
all_Y = data.y.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} States correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas
        print(missing_states)
        break
    if answer_state in all_states:
        index = all_states.index(answer_state)
        x_cor = all_x[index]
        y_cor = all_Y[index]

        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        name.goto(x_cor, y_cor)
        name.write(answer_state)
        guessed_states.append(answer_state)

screen.exitonclick()


