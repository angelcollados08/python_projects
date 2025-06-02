# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column('pokemon name' , ['Pikachu','Squirtle','Charmander'])
table.add_column('type' , ['Electric','Water','Fire'])
table.align = "c"
print(table)
