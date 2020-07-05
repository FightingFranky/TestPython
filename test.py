import pgzrun

RED = 200, 0, 0
BOX = Rect((100, 20), (200, 100))

ls = []

def draw():
    screen.draw.rect(BOX, RED)

pgzrun.go()