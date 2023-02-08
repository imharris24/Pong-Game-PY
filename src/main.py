import turtle

# function for moving paddle up
def movePaddleUp(paddle):
    y = (paddle.ycor() + 20)
    if y > 260:
        y = 260
    paddle.sety(y)

# function for moving paddle down
def movePaddleDown(paddle):
    y = (paddle.ycor() - 20)
    if y < -260:
        y = -260
    paddle.sety(y)

# window setup
window = turtle.Screen()
window.title('Pong')
window.setup(width=800, height=600)
window.bgcolor('black')
window.tracer(0)

# creating score board
scoreA = 0
scoreB = 0
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.hideturtle()
scoreBoard.penup()
scoreBoard.color('white')
scoreBoard.goto(0, 260)
scoreBoard.write(f'Player 1 : {scoreA}  |  Player 2 : {scoreB}', align='center', font=('Arial', 12, 'bold'))

# creating bar A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_len=1, stretch_wid=4)
paddleA.penup()
paddleA.goto(-350, 0)

# creating bar B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_len=1, stretch_wid=4)
paddleB.penup()
paddleB.goto(350, 0)

# creating ball
ball = turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

# defining controls
window.listen()
window.onkeypress(lambda: movePaddleUp(paddleA), 'w')
window.onkeypress(lambda: movePaddleDown(paddleA), 's')
window.onkeypress(lambda: movePaddleUp(paddleA), 'W')
window.onkeypress(lambda: movePaddleDown(paddleA), 'S')
window.onkeypress(lambda: movePaddleUp(paddleB), 'Up')
window.onkeypress(lambda: movePaddleDown(paddleB), 'Down')

# main loop
while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
    if ball.xcor() > 405 or ball.xcor() < -405:
        if (ball.xcor() > 0):
            scoreA += 1
        else:
            scoreB +=1
        ball.goto(0, 0)
        ball.dx *= -1
        scoreBoard.clear()
        scoreBoard.write(f'Player 1 : {scoreA}  |  Player 2 : {scoreB}', align='center', font=('Arial', 12, 'bold'))
    if (ball.xcor() >= 330 and ball.xcor() <= 340) and (ball.ycor() <= paddleB.ycor() + 50 and ball.ycor() >= paddleB.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() <= -330 and ball.xcor() >= -340) and (ball.ycor() <= paddleA.ycor() + 50 and ball.ycor() >= paddleA.ycor() - 50):
        ball.dx *= -1
