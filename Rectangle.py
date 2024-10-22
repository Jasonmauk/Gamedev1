import pgzrun
import random

WIDTH = 1000
HEIGHT = 1000
TITLE = 'Hello'

def draw():
    r = 255
    g = 0
    b = random.randint(120,255)
    width = WIDTH-200
    height = HEIGHT-200
    for i in range(30):
        rect = Rect((0,0),(width,height))
        rect.center = 500,500
        screen.draw.rect(rect,(r,g,b))
        r -= 10
        g +=10
        width -= 10
        height-= 10
    

pgzrun.go()
