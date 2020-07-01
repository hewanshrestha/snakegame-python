import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#setting up the screen
sc = turtle.Screen()
sc.title("Snake Game")
sc.bgcolor("white")
sc.setup(width=800,height=600)
sc.tracer(0)    #turns off the updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "right"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0  High Score : 0",align="center",font=("Courier",24,"normal"))

#functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#keyboard bindings
sc.listen()
sc.onkeypress(go_up,"Up")
sc.onkeypress(go_down,"Down")
sc.onkeypress(go_left,"Left")
sc.onkeypress(go_right,"Right")


#main game loop
while True:
    sc.update()

    # check for collision with border
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segments list
        segments.clear()

        # reset the delay
        delay = 0.1

        # reset the score
        score = 0
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

       
    # check for collision with food
    if head.distance(food) < 20:
        #move food to random place
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        # check the high score
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    
    #move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    #move segment 0 to where the head moves
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision of head with segments
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            # clear the segments list
            segments.clear()

            # reset the delay
            delay = 0.1

            # reset the score
            score = 0
            pen.clear()
            pen.write("Score : {}  High Score : {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        

    time.sleep(delay)


sc.mainloop()