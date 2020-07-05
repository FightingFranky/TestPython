import pgzrun
import time

alien = Actor('alien')
alien.topright = 0, 10
alien.angle = 0

WIDTH = 1000
HEIGHT = alien.height + 1000


def draw():
    screen.draw.text("是我了", (0, 0), color='black')
    screen.clear()
    screen.fill((128, 0, 0))
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.left = 0



def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("EKK")
        tone.play('C3')
        set_hurt()
    else:
        print("九折")


def set_hurt():
    alien.image = "hurt"
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = "alien"


pgzrun.go()
