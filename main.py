from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Welcome to Snake game")
screen.tracer(0)

# goto = 0
# for _ in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.setposition(x= 0 - goto, y= 0)
#     goto +=20 
    

snake = Snake()
is_game_on = True


while is_game_on:
     screen.update()
     time.sleep(0.1)
     snake.move()
    #  segments[0].left(90)
       
        












screen.exitonclick()