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
player_1.color("green")
player_1.shapesize(stretch_len=6, stretch_wid=3)
player_1.penup()
player_1.goto(-350, 0)


#player_2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("green")
player_2.shapesize(stretch_len=6, stretch_wid=3)
player_2.penup()
player_2.goto(350, 0)

while True:
    window.update()
