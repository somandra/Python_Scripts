import turtle
import os
import random

#Create a screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space Invader")
#Draw a border
border_pen = turtle.Turtle()
border_pen.speed(20)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for s in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.penup()
border_pen.setposition(-100,250)
border_pen.pendown()
border_pen.pensize(2)
border_pen.fd(200)
border_pen.hideturtle()

#create a player1

player1 = turtle.Turtle()
player1.color("red")
player1.shape("triangle")
player1.penup()
player1.speed(20)
player1.setposition(-50,-250)
player1.setheading(90)

player1_speed = 15

#create a player1

player2 = turtle.Turtle()
player2.color("yellow")
player2.shape("triangle")
player2.penup()
player2.speed(20)
player2.setposition(50,-250)
player2.setheading(90)

player2_speed = 15

#Move player1 left
def mov_left():
    x = player1.xcor()
    x-=player1_speed
    if x<-280:
        x=-280
    player1.setx(x)
#move player1 right
def mov_right():
    x = player1.xcor()
    x+=player1_speed
    if x>280:
        x=280
    player1.setx(x)
#create keyboard bindings
turtle.listen()
turtle.onkey(mov_left,"Left")
turtle.onkey(mov_right,"Right")


while True:
    y1 = player1.ycor()
    s1 = random.randint(5, 10)
    y1 += s1
    player1.sety(y1)

    y2 = player2.ycor()
    s2 = random.randint(5, 10)
    y2 += s2
    player2.sety(y2)


    if (y2 >= 250) or (y1 >= 250):
            if y1>=250:
                turtle.color('red')
                style = ('Courier', 30, 'italic')
                turtle.write('Red turtle won!', font=style, align='center')
                turtle.hideturtle()
                break
            else:
                turtle.color('deep pink')
                style = ('Courier', 30, 'italic')
                turtle.write('Yellow turtle won!', font=style, align='center')
                turtle.hideturtle()
                break









wn.mainloop()