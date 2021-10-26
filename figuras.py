import math
from turtle import *


speed(0)

color("red")
fillcolor("green")

s = 200 #tamaño cuadrado

#cuadrado
for i in range(4):
    fd(s)
    left(90)


#triángulo
theta = 60
r = math.sqrt((s**2)+((s/2)**2))
left(theta)
fd(r)


done()