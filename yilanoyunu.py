import turtle
import time
import random 

hiz = 0.15

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgpic('toprak.gif')
pencere.setup(width=600, height=600)
pencere.tracer(0) 

turtle.register_shape('yilankafayukari.gif')
turtle.register_shape('yilankafasol.gif')
turtle.register_shape('yilankafasag.gif')
turtle.register_shape('yilankafaasagi.gif')
turtle.register_shape('elma.gif')

kafa = turtle.Turtle()
kafa.shape('yilankafaasagi.gif')
kafa.speed(0)
kafa.shapesize(1.0, 1.0, 1)
kafa.setheading(90)
kafa.penup()
kafa.goto(0,100)
kafa.direction = 'stop'

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape('elma.gif')
yemek.color('red')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

kuyruklar = []

puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y+20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y-20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x+20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x-20)

def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'
        kafa.shape('yilankafayukari.gif')

def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'
        kafa.shape('yilankafaasagi.gif')

def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'
        kafa.shape('yilankafasag.gif')

def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'
        kafa.shape('yilankafasol.gif')

pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = 'stop'

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)

        kuyruklar = []
        puan = 0
        hiz = 0.15
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

    if kafa.distance(yemek) < 20:
        x = random.randint(0, 14)*20
        y = random.randint(0, 14)*20
        yemek.goto(x, y)

        puan = puan + 10
        hiz = hiz - 0.003
        yaz.clear()
        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('circle')
        yeniKuyruk.color('green')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for i in kuyruklar:
        if i.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(-200, 0)
            kafa.direction = 'stop'

            for kuyruk in kuyruklar:
                kuyruk.goto(1000, 1000)
            
            kuyruklar = []
            puan = 0
            hiz = 0.15
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))


    time.sleep(hiz)