import turtle


window = turtle.Screen()
window.title("Pong Pong")
window.bgpic("/home/o11q/Desktop/git clone/py-pong/pong-game/backgroung.gif")
window.setup(width=800, height=500)
window.tracer(0)

#player_1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("red")
player_1.shapesize(stretch_wid=4, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)


#player_2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("red")
player_2.shapesize(stretch_wid=4, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("mediumseagreen")
ball.penup()
ball.goto(0, 0)

#ft
#up
def player_1_u():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

#down
def player_1_d():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)

#up2
def player_2_u():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

#down2
def player_2_d():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


#Kinput
window.listen()
window.onkeypress(player_1_u, "w")

window.listen()
window.onkeypress(player_1_d, "s")

#Kinput2
window.listen()
window.onkeypress(player_2_u, "i")

window.listen()
window.onkeypress(player_2_d, "k")
while True:
    window.update()
