import pgzrun
import turtle
import random

isLoose = False

background1 = Actor("bg1")
background1.pos = (300, 300)
hero1 = Actor("prince")
hero1.pos = (300, 300)

WIDTH = 1000
HEIGHT = 606
step = 0


def draw():
    global t, isLoose
    screen.fill('white')
    screen.draw.text("Welcome to the Jungle Adventure\n"
                     "  Press  J  start  the  new  game\n"
                     "  Press  K  continue  the  game\n"
                     "  Press  L  exit  the  game", (200, 200), fontsize=50, color="orange")
    if step == 1:
        screen.clear()
        screen.fill('white')
        background1.draw()
        hero1.draw()

    # elif step == 2:
    if step == 3:
        isLoose = True
        screen.clear()
        screen.fill('white')
        screen.draw.text("You have losed your game, please exit!", (200, 200), fontsize=50, color="orange")
    if step == 4:
        screen.clear()
        screen.fill('white')
        background1.draw()

    if step == 5:
        screen.clear()
        background1.draw()
        screen.fill('white')
        hero1.up += 1
        hero1.draw()

    if step == 6:
        screen.clear()
        background1.draw()
        screen.fill('white')
        hero1.right += 1
        hero1.draw()

    if step == 7:
        screen.clear()
        background1.draw()
        screen.fill('white')
        hero1.up += 1
        hero1.draw()


def on_key_down(key):
    global step
    if key == keys.J:
        step = 1
    elif key == keys.K:
        step = 2
    elif key == keys.L:
        step = 3
    elif key == keys.A:
        step = 4
    elif key == keys.S:
        step = 5
    elif key == keys.D:
        step = 6
    elif key == keys.W:
        step = 7


def update():
    if random.randrange(60) == 0:
    global step
    if step == 4:
        hero1.x -= 2
        left_movement()
    if step == 6:
        hero1.x += 2

def front_movement():
    hero1.image = 'prince'

def right_movement():
    hero1.image = 'prince_right'
    clock.schedule_unique(front_movement, 1.0)


def left_movement():
    hero1.image = 'prince_left'
    clcok.schedule_unique(front_movement, 1.0)



pgzrun.go()
