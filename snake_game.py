import turtle
import time
import random
delay=0.1

# Window
wn = turtle.Screen()
wn.title("Snake Game by Nasaj")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments=[]



#Functions

def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"        




def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y +20)
    
    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction =="left":
        x=head.xcor()
        head.setx(x -20)
    if head.direction =="right":
        x=head.xcor()
        head.setx(x +20)

#Keyboard binding
wn.listen()
wn.onkeypress(go_up,"w")                
wn.onkeypress(go_down,"s")                
wn.onkeypress(go_left,"a")                
wn.onkeypress(go_right,"d")                

# Main game loop function
def game_loop():
    wn.update()

    # Move the body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Move the head EVERY TIME
    move()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    wn.ontimer(game_loop, int(delay * 1500))

game_loop()
wn.mainloop()
