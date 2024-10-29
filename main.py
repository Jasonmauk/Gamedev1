import pgzrun
import random


TITLE = "SHOOT THE ALIEN"
WIDTH = 500
HEIGHT = 500

msg = ""

alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color=(200,12,30))
    alien.draw()
    screen.draw.text(msg,center = (240,200),fontsize=30, color ='yellow')

   

def place_alien():
    alien.x = random.randint(50,450)
    alien.y = random.randint(50,450)

def on_mouse_down(pos):
    global msg 
    if alien.collidepoint(pos):
        msg = "Good shot!"
        place_alien()
    else:
        msg = "Off target, Try again!"


place_alien()

pgzrun.go()