import turtle
import time
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
    wn.ontimer(game_loop, 100)  # repeat every 100ms
    move()
    time.sleep(delay)

game_loop()
wn.mainloop()
