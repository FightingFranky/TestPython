import pgzrun
import turtle
import random
import math


# HP类，可用于王子及小怪
class HP(object):
    def __init__(self, FullHP, num):
        self.FullHP = FullHP
        self.CurrentHP = FullHP
        self.num = num  #命数
        self.count = 1  #复活次数

    #判断是否死亡并在可能的情形下复活
    def isdead(self):
        if self.CurrentHP > 0:
            return
        elif self.CurrentHP <= 0 and self.count < self.num:  #能复活
            self.CurrentHP = self.FullHP
            self.count += 1
            hero.pos = (0, 0)
            return
        else:
            return True



isLoose = False
speed_x = 2
speed_y = 2
standard_speed = 2

background1 = Actor("bg1")  # 896, 448
background1.pos = 500, 300

hero = Actor("prince")
prince_HP = HP(10, 1)  #初始化王子HP

monsters = []
monster = Actor("red_din")

n = 3
boxes = []
for _ in range(n):
    boxes.append(Actor('box_close'))
dx = []
dy = []

coins = 0

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


def game_over():
    pass


# 画血条
def draw_hp_bar():
    global step
    if (prince_HP.isdead()):
        step = 3
    HPBar = Rect((20, 20), (200, 35))  #血槽
    CurrentHPBar = Rect(
        (20, 20), (200 * prince_HP.CurrentHP / prince_HP.FullHP, 33))  #当前血量
    screen.draw.rect(HPBar, 'black')
    screen.draw.filled_rect(CurrentHPBar, 'black')


# 画金币
def draw_coins_bar():
    screen.blit('gloden', (20, 60))  #20,60
    screen.draw.text(str(coins), (125, 77), fontsize=50)  #125 77


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
        screen.draw.text(
            "Welcome to the Prince V.S. Monsters Game\n"
            "  Press  Number  1  to  start  the  new  game\n"
            "  Press  Number  2  to  continue  the  game\n"
            "  Press  Number  3  to  exit  the  game", (200, 200),
            fontsize=50,
            color="orange")
    if step != 99:
        screen.clear()
        screen.fill('white')
        background1.draw()
        hero.draw()
        screen.draw.text("Press Number 3 to exit the game", (80, 0),
                         fontsize=25,
                         color='orange')
        monster.draw()

    # elif step == 2:
    if step == 3:
        isLoose = True
        screen.clear()
        screen.fill('white')
        screen.draw.text("You have losed your game, please exit!", (200, 200),
                         fontsize=50,
                         color="orange")
        clock.schedule(exit, 3)
    ### 上下左右移动模块 ####
    if step == 4 or step == 5 or step == 6 or step == 7:
        background1.draw()
        monster.draw()
        for i in range(3):
            boxes[i].pos = (dx[i], dy[i])
            boxes[i].draw()
        # 优先级最高
        hero.draw()
        #HP、金币状态绘制
        draw_hp_bar()
        draw_coins_bar()
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

    #靠近至一定距离时怪兽主动接近
    if monster.distance_to(hero) < 200:
        '''#if random.randint(1,6) == 1:
        speed_x = standard_speed**1.5 * math.cos(monster.angle_to(hero))
        speed_y = -standard_speed**1.5 * math.sin(monster.angle_to(hero))'''
        if monster.x > hero.x:
            monster.x -= speed_x
        elif monster.x < hero.x:
            monster.x += speed_x
        else:
            speed_y = standard_speed**1.5
        speed_x = standard_speed

        if monster.y > hero.y:
            monster.y -= speed_y
        elif monster.y < hero.y:
            monster.y += speed_y
        else:
            speed_x = standard_speed**1.5
        speed_y = standard_speed

    else:
        #平均2s一次的随机转向
        if random.randint(1, 120) == 1:
            ang = random.randint(-180, 180)
            speed_x = standard_speed**1.5 * math.cos(ang)
            speed_x = -standard_speed**1.5 * math.sin(ang)
        monster.x += speed_x
        monster.y += speed_y

    if WIDTH <= monster.x or monster.x <= 0:
        speed_x *= -1
    if HEIGHT <= monster.y or monster.y <= 0:
        speed_y *= -1

    #### 简单的四边跑 ######
    if hero.colliderect(monster):
        tone.play('G2', 0.5)
        prince_HP.CurrentHP -= 0.05
    for i in range(3):
        if hero.colliderect(boxes[i]):
            boxes[i].image = 'box_open'


pgzrun.go()
