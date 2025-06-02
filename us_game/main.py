import turtle
import pandas
FONT = ('Arial', 7, 'normal')
ALINGMENT = "center"
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S GAME")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
n_correct = 0
#answer_state = screen.textinput(title=f"{n_correct}/50 States Correct", prompt="whats another state name")
answer_list = []
missing_state = []
all_states = data.state.to_list()
while n_correct < 50:
    answer_state = screen.textinput(title=f"{n_correct}/50 States Correct", prompt="whats another state name")
    if answer_state == "Exit":
        for state in all_states:
            missing_state = [state for state in all_states if state not in answer_list]
            new_data_frame = pandas.DataFrame(missing_state)
            new_data_frame.to_csv("states to learn")
        print(missing_state)
        break
    print(answer_state)
    data_table = data[data["state"] == answer_state]
    if data_table.size > 0:
        if (answer_state not in answer_list):
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(int(data_table.x),int(data_table.y))
            t.write(data_table.state.item(), False, align=ALINGMENT, font=FONT)
            n_correct +=1


screen.exitonclick()