import turtle
import time
import random

#  _______________________
# Game Window
#  _______________________

window = turtle.Screen()
window.bgcolor("black")
window.title("Game Snake For Me")
window.setup(width=800,height=800)
window.tracer(0)
# _________________________
# Creating The Snake Game
# _________________________

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"

# ___________________
# Creating snake food
# ___________________

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,120)

# ___________________
# Creating the snake body
# ___________________

segments=[]
# ___________________
# scoreboard
# ___________________
score=0
high_score=0

pen=turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,300)


pen.write(
    "Score: 0       High_score: 0",
    align="center",
    font=("Arial", 30, "bold")

)
# __________________
# Movement Function
# __________________

def go_up():
    if head.direction !='down':
        head.direction='up'

def go_down():
    if head.direction !='up':
        head.direction='down'

def go_left():
    if head.direction !='right':
        head.direction='left'

def go_right():
    if head.direction !='left':
        head.direction='right'


# _______________________
# Movement The Snake Head
# _______________________


def move():

        x= head.xcor()
        y= head.ycor()

        if head.direction=='up':
            head.sety(y+20)

        if head.direction=='down':
            head.sety(y-20)

        if head.direction=='right':
            head.setx(x+20)

        if head.direction=='left':
            head.setx(x-20)



# __________________
# Keyboard Control
# __________________

window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_right,"Right")
window.onkeypress(go_left,"Left")


# ___________________
# Main Game Loop
# ___________________

while True:
    window.update()

    # _______________
    # wall collision
    # _______________

    if (
            head.xcor() > 390
            or head.xcor() < -390
            or head.ycor() > 390
            or head.ycor() < -390
    ):

        time.sleep(1)

        head.goto(0,0)
        head.direction='stop'


        for segment in segments:
            segment.goto(1200,1200)
        segments.clear()

        score=0
        pen.clear()


        pen.write(
            f"score:{score}     high_score:{high_score} ",
            align="center",
            font=('Arial', 30,"bold")

        )

    # __________________
    # Food Collision
    # __________________

    if head.distance(food)<20:
        x=random.randint(-390,390)
        y=random.randint(-390,390)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()


        segments.append(new_segment)

        score+=1


        if score>high_score:
            high_score=score

        pen.clear()

        pen.write(
            f"score:{score}     high_score:{high_score} ",
            align="center",
            font=('Arial', 30, "bold")
        )


    # __________________
    # Movement The Snake Body
    # __________________

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()

        segments[index].goto(x,y)


    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()


    # _______________
    # Self Collision
    # _______________


    for segment in segments[1:]:

        if segment.distance(head)<20:
            time.sleep(1)

            head.goto(0,0)
            head.direction='stop'
            for part in segments:
                part.goto(1200,1200)

            segments.clear()


            score=0
            pen.clear()
            pen.write(

                f"score:{score} high_score:{high_score} ",
                align="center",
                font=('Arial', 30, "bold")
            )
    time.sleep(0.1)

window.mainloop()

























