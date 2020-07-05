import pgzrun
import turtle
import random

isLoose = False
speed_x = 2
speed_y = 2


background1 = Actor("bg1") # 896, 448
background1.pos = 500, 300

hero = Actor("prince")

monster = Actor("red_din")

box = Actor('box_close')
dx = []
dy = []

for i in range(5):
    a = random.randint(50, 800)
    b = random.randint(50, 400)
    dx.append(a)
    dy.append(b)


WIDTH = background1.width + 100
HEIGHT = background1.height + 100
step = 99

monster.x = WIDTH / 2
monster.y = HEIGHT / 2

### 上下左右行走模块函数 ###
def left_movement():
    hero.image = "prince_left"

def right_movement():
    hero.image = "prince_right"

def up_movement():
    hero.image = "prince_back"

def down_movement():
    hero.image = "prince"
####################

def draw():
    global step, isLoose
    screen.fill('white')
    if step == 99:
        screen.draw.text("Welcome to the Prince V.S. Monsters Game\n"
                         "  Press  Number  1  to  start  the  new  game\n"
                         "  Press  Number  2  to  continue  the  game\n"
                         "  Press  Number  3  to  exit  the  game", (200, 200), fontsize=50, color="orange")
    if step != 99:
        screen.clear()
        screen.fill('white')
        background1.draw()
        hero.draw()
        screen.draw.text("Press Number 3 to exit the game", (80, 0), fontsize=25, color='orange')
        monster.draw()

    # elif step == 2:
    if step == 3:
        isLoose = True
        screen.clear()
        screen.fill('white')
        screen.draw.text("You have losed your game, please exit!", (200, 200), fontsize=50, color="orange")
        exit()
    ### 上下左右移动模块 ####
    if step == 4 or step == 5 or step == 6 or step == 7:
        background1.draw()
        monster.draw()
        for i in range(3):
            box.pos = dx[i], dy[i]
            box.draw()
        # 优先级最高
        hero.draw()
        if step == 4:
            clock.schedule(right_movement, 0.01)
        if step == 5:
            clock.schedule(left_movement, 0.01)
        if step == 6:
            clock.schedule(up_movement, 0.01)
        if step == 7:
            clock.schedule(down_movement, 0.01)
    #################################


def on_key_down(key):
    global step
    step = 0
    if key == keys.K_1:
        step = 1
    elif key == keys.K_2:
        step = 2
    elif key == keys.K_3:
        step = 3
        exit()

def update():
    global step, hero, speed_x, speed_y
    # 往右走
    if keyboard.D:
        hero.x += 5
        if hero.x >= WIDTH:
            hero.x = WIDTH - 30
        step = 4
    elif keyboard.A:
        if hero.x < 0:
            hero.x = 0 + 30
        hero.x -= 5
        step = 5
    elif keyboard.W:
        if hero.y < 0:
            hero.y = 0 + 30
        hero.y -= 5
        step = 6
    elif keyboard.S:
        if hero.y >= HEIGHT:
            hero.y = HEIGHT - 30
        hero.y += 5
        step = 7
    ##### 怪兽自己走模块 #####
    # monster.pos = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    monster.x += speed_x
    monster.y += speed_y
    if WIDTH <= monster.x or monster.x <= 0:
        speed_x *= -1
    if HEIGHT <= monster.y or monster.y <= 0:
        speed_y *= -1
    #### 简单的四边跑 ######
    if hero.colliderect(monster):
        tone.play('G2', 0.5)
    if hero.colliderect(box):
       box.image = 'box_open'






pgzrun.go()
