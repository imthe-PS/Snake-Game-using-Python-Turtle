# Import required modules

import turtle
import random
import time

# Generate head

head = turtle.Turtle()
head.shape("square")
head.color("black")
head.speed(5)
head.penup()
head.goto(0,100)
head.direction = "stop"

# delay

delay = 0.1

#score

score = 0
high_score = 0

# Generate window

win = turtle.Screen()
win.title("Snake : I need food")
win.bgcolor("skyblue")
win.tracer(0)
win.setup(600,600)

# Moving the head

def go():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"
        
# Linking with keyboard

win.listen()
win.onkey(go_up, 'w')
win.onkey(go_down, 's')
win.onkey(go_right, 'd')
win.onkey(go_left, 'a')

# Pizza as Food

pizza = turtle.Turtle()
pizza.shape("circle")
pizza.color("red")
pizza.speed(0)
pizza.penup()
pizza.goto(0,0)
pizza.shapesize(0.6, 0.6)

# Score

points = turtle.Turtle()
points.speed(0)
points.shape("square")
points.color("white")
points.penup()
points.hideturtle()
points.goto(0,260)
points.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

# Segment

segments = []

# Colors
# Colors = ['red', 'blue', 'purple', 'green', 'yellow', 'skyblue']

while True:
    win.update()
    if head.distance(pizza) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        pizza.goto(x,y)
        new_segment = turtle.Turtle()
        #new_segment.color(random.choice(colors))
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
            
        points.clear()
        points.write("score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    for i in range(len(segments) -1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
# Check for collision

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
# Hide the segments

        for segment in segments:
            segment.goto(1000,1000)
        segments = []
        
        score = 0
        points.clear()
        points.write("score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    go()

# Add body collision

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments = []
            score = 0
            points.clear()
            points.write("score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
