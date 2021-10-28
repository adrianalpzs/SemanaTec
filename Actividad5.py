from random import *
from turtle import *
from freegames import path

"""
Como un condimento de innovación al juego, 
Podrías utilizar algo diferente a los dígitos 
para resolver el juego y que al usuario le ayude a tener mejor memoria ?
"""
#Sí, añadiendo colores

car = path('car.gif') 
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
click_count = 0
end = False
change_tiles = False
colores = ['#FFEBEE', '#F8BBD0', '#E1BEE7',  '#D1C4E9', '#C5CAE9', 
	   '#BBDEFB', '#B3E5FC', '#B2EBF2', '#B2DFDB', '#C8E6C9',
	   '#DCEDC8', '#F0F4C3', '#FFF9C4', '#FFECB3', '#FFE0B2',
	   '#FFCCBC', '#D7CCC8', '#E53935', '#D81B60', '#8E24AA',
	   '#5E35B1', '#3949AB', '#1E88E5', '#039BE5', '#00ACC1',
	   '#00897B', '#43A047', '#7CB342', '#C0CA33', '#FDD835',
	   '#FFB300', '#FB8C00', '#F4511E']

def square(x, y, txt):
    "Draw white square with black outline at (x, y)."
    global change_tiles
    up()
    goto(x, y)
    down()
    color('black', txt)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 230) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 230

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global click_count
    global change_tiles
    global end
    spot = index(x, y)
    mark = state['mark']

    if y<168:
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            if not end:
                click_count +=1 
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None
    else:
        change_tiles = not change_tiles

def draw():
    "Draw image and tiles."
    global click_count
    global end
    clear()
    goto(0, -30)
    shape(car)
    if True not in hide:
        end = True
        text = "Has ganado con " + str(click_count) + " intentos"  
    else:
        text = "Número de intentos: "+ str(click_count) 
        
    stamp()
    penup()
    goto(-197, 173)
    pendown()
    color('black','white')
    begin_fill()

    for count in range(2):
        forward(320)
        left(90)
        forward(60)
        left(90)
    
    penup()
    goto(125, 173)
    pendown()
    
    for count in range(2):
        forward(60)
        left(90)
        forward(60)
        left(90)

    end_fill()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count) 
            square(x, y, 'white')

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        square(x, y, colores[tiles[mark]])
        up()
        goto(x + 27, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')
    
    penup()
    goto(-35, 190)
    pendown()
    write(text, font=('Arial', 18, 'normal'), align='center')
    penup()
    goto(157, 177)
    pendown()
    write("click me \nto add \ncolor", font=('Arial', 10, 'normal'), align='center')

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 480, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()