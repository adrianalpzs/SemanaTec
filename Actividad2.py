#Actividad 2 Juego de la vibora
#Adriana Ines Lopez Sanchez
#Michelle Rayas Guevara

#Bibliotecas
from turtle import *
from random import randrange
from freegames import square, vector
import random

#Colores para vibora y comida
colors=['blue', 'green', 'purple','yellow','orange']

#Designar color a vibora (aleatorio)
bodyc=random.choice(colors)

#Designar color a comida (aleatorio)
foodc=random.choice(colors)

if foodc==bodyc:
    foodc=random.choice(colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#La comida se mueve en aletorio dentro de la ventana
def mFood():
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    ontimer(mFood, 4500)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, bodyc)

    square(food.x, food.y, 9, foodc)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
mFood()
move()
done()
