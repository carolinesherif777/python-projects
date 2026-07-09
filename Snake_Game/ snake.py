import turtle
import random
import time

# -------------------------------
# Game Window Setup
# -------------------------------

window = turtle.Screen()
window.title("Snake Game For Me")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(0)

# -------------------------------
# Creating the Snake Head
# -------------------------------

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# -------------------------------
#Creating the Food
# -------------------------------

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 120)

# -------------------------------
# Creating the Snake Body
# -------------------------------

segments = []

# -------------------------------
# Scoreboard
# -------------------------------

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)

pen.write(
    "Score: 0  High Score: 0",
    align="center",
    font=("Arial", 30, "bold")
)

# -------------------------------
# Movement Functions
# -------------------------------

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


# -------------------------------
# Moving the Snake Head
# -------------------------------

def move():

    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(y - 20)

    if head.direction == "left":
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(x + 20)


# -------------------------------
# Keyboard Controls
# -------------------------------

window.listen()

window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# -------------------------------
# Main Game Loop
# -------------------------------

while True:

    window.update()

    # ---------------------------
    # Wall Collision
    # ---------------------------

    if (
        head.xcor() > 390
        or head.xcor() < -390
        or head.ycor() > 390
        or head.ycor() < -390
    ):

        time.sleep(1)

        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1200, 1200)

        segments.clear()

        score = 0

        pen.clear()

        pen.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 20, "bold")
        )

    # ---------------------------
    # Food Collision
    # ---------------------------

    if head.distance(food) < 20:

        x = random.randint(-380, 380)
        y = random.randint(-380, 380)

        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()

        segments.append(new_segment)

        score += 1

        if score > high_score:
            high_score = score

        pen.clear()

        pen.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 20, "bold")
        )

    # ---------------------------
    # Moving the Snake Body
    # ---------------------------

    for index in range(len(segments) - 1, 0, -1):

        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()

        segments[index].goto(x, y)

    if len(segments) > 0:

        x = head.xcor()
        y = head.ycor()

        segments[0].goto(x, y)

    move()

    # ---------------------------
    # Self Collision
    # ---------------------------

    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for part in segments:
                part.goto(1200, 1200)

            segments.clear()

            score = 0

            pen.clear()

            pen.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Arial", 20, "bold")
            )

    time.sleep(0.1)

window.mainloop()
