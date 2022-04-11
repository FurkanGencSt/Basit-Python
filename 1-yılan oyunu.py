
import turtle,random,time


delay = 0.15
tails = []
score = 0

screen = turtle.Screen() 
screen.tracer(0)
screen.setup(width= 600, height=800)
screen.bgcolor('lightgreen')
screen.title("Sneak Game")


frame1 = turtle.Turtle() #Down
frame1.penup()
frame1.shape('square')
frame1.shapesize(1,29)
frame1.color('gray')
frame1.goto(0,-280)
frame1.direction = "stop"

frame2 = turtle.Turtle() #Up
frame2.penup()
frame2.shape('square')
frame2.shapesize(1,29)
frame2.color('gray')
frame2.goto(0,280)
frame2.direction = "stop"

frame3 = turtle.Turtle() #Right
frame3.penup()
frame3.shape('square')
frame3.shapesize(29,1)
frame3.color('gray')
frame3.goto(285,0)
frame3.direction = "stop"

frame4 = turtle.Turtle() #Left
frame4.penup()
frame4.shape('square')
frame4.shapesize(29,1)
frame4.color('gray')
frame4.goto(-290,0)
frame4.direction = "stop"






head = turtle.Turtle()
head.color('black')
head.shape('square')
head.speed(0)
head.penup()
head.direction = "stop"
head.goto(0,0)

food = turtle.Turtle()
food.shape('circle')
food.shapesize(0.80,0.80)
food.color('red')
food.penup()
food.direction = "stop"
food.goto(0,100)
food.speed(0)

write = turtle.Turtle()
write.hideturtle()
write.penup()
write.color('white')
write.goto(0,300)
write.direction = "stop"
write.write("Score: {}".format(score), align= 'center', font=('Courier', 24, 'normal'))






def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
            
def goUp():
    if head.direction != 'down':
        head.direction = 'up'
def goDown():
    if head.direction != 'up':
        head.direction = 'down'
def goLeft():
    if head.direction != 'right':
        head.direction = 'left'
def goRight():
    if head.direction != 'left':
        head.direction = 'right'

screen.listen()
screen.onkey(goUp, 'Up')
screen.onkey(goDown, 'Down')
screen.onkey(goLeft, 'Left')
screen.onkey(goRight, 'Right')



while True:
    screen.update()
    
    if head.xcor() > 270 or head.xcor() < -270 or head.ycor() > 270 or head.ycor() < -270:
        head.goto(0,0)
        head.direction = "stop"
        for tail in tails:
            tail.goto(1000,1000)
        tails = []
        score = 0
        write.clear()
        write.write("Score: {}".format(score), align= 'center', font=('Courier', 24, 'normal'))
    

    if head.distance(food) < 15:
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        food.goto(x,y)

        score = score + 10
        write.clear()
        write.write("Score: {}".format(score), align= 'center', font=('Courier', 24, 'normal'))

        newtail = turtle.Turtle()
        newtail.color('white')
        newtail.shape('square')
        newtail.penup()
        newtail.shapesize(0.90,0.90)
        tails.append(newtail)

    for i in range(len(tails) -1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x,y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)   
    
    move()
    time.sleep(delay)