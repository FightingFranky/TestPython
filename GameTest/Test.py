import pgzrun
from HP import *
WIDTH = 1200
HEIGHT = 600

Anims = [Actor('prince'), Actor('prince_right'), Actor('prince')]
Anims1 = [Actor('prince'), Actor('prince_left'), Actor('prince')]
Anims2 = [Actor('prince'), Actor('prince_back'), Actor('prince')]
Anims3 = [Actor('prince'), Actor('prince'), Actor('prince')]
numAnims = len(Anims)
animIndex = 0
animSpeed = 0
t = 0
prince_HP = HP(10, 3)#初始化王子HP
coins = 0


player_x = WIDTH / 10
player_y = HEIGHT / 3
last_player_x = 0
last_player_y = 0

for i in range(numAnims):
    Anims[i].x = player_x
    Anims[i].y = player_y
    Anims1[i].x = player_x
    Anims1[i].y = player_y

for j in range(numAnims):
    Anims2[j].x = player_x
    Anims2[j].y = player_y
    Anims3[j].x = player_x
    Anims3[j].y = player_y

# HP类，可用于王子及小怪
class HP(object):

    def __init__(self, FullHP, num):
        self.FullHP = FullHP
        self.CurrentHP = FullHP
        self.num = num #命数
        self.count = 0 #复活次数
    
    #判断是否死亡并在可能的情形下复活
    def isdead(self):
        if self.CurrentHP > 0:
            return
        elif self.CurrentHP <= 0 & self.count < self.num: #能复活
            self.CurrentHP = self.FullHP
            return
        else:
            return True

def game_over():
    pass

def draw_hp_bar():
    #画血条
    prince_HP.isdead()
    HPBar = Rect((20, 20), (200, 35)) #血槽
    CurrentHPBar = Rect((20, 20), (200*prince_HP.CurrentHP/prince_HP.FullHP, 33)) #当前血量
    screen.draw.rect(HPBar, 'black')
    screen.draw.filled_rect(CurrentHPBar, 'black')

def draw_coins_bar():
    screen.blit('gloden', (20,60))
    screen.draw.text(str(coins), (125, 77), fontsize=50)


def draw():
    global t
    screen.fill('gray')

    draw_hp_bar() #画血条函数
    draw_coins_bar() #画金币函数

    if t == 1:
        Anims[animIndex].draw()
    if t == 2:
        Anims1[animIndex].draw()
    if t == 3:
        Anims2[animIndex].draw()
    if t == 4:
        Anims3[animIndex].draw()


def update():
    global animIndex, player_x, animSpeed, t, player_y, last_player_x, last_player_y
    #测试减血
    prince_HP.CurrentHP -= 0.05
    # 往右走
    if keyboard.D:
        t = 1
        player_x = last_player_x
        player_y = last_player_y
        player_x += 5
        for i in range(numAnims):
            Anims[i].x = player_x
        if player_x >= WIDTH:
            player_x = 0
        animSpeed += 1
        if animSpeed % 10 == 0:
            animIndex += 1
            if animIndex >= numAnims:
                animIndex = 0
        last_player_x = player_x
    # 往左走
    if keyboard.A:
        t = 2
        player_x = last_player_x
        player_y = last_player_y
        player_x -= 5
        for i in range(numAnims):
            Anims1[i].x = player_x
        if player_x < 0:
            player_x = WIDTH
        animSpeed += 1
        if animSpeed % 10 == 0:
            animIndex += 1
            if animIndex >= numAnims:
                animIndex = 0
        last_player_x = player_x
    # 往上走
    if keyboard.W:
        t = 3
        player_x = last_player_x
        player_y = last_player_y
        player_y -= 5
        for i in range(numAnims):
            Anims2[i].y = player_y
        if player_y < 0:
            player_y = HEIGHT
        # 控制动画变化速度
        animSpeed += 1
        if animSpeed % 15 == 0:
            animIndex += 1
            if animIndex >= numAnims:
                animIndex = 0
        last_player_y = player_y
    # 往下走
    if keyboard.S:
        t = 4
        player_x = last_player_x
        player_y = last_player_y
        player_y += 5
        for i in range(numAnims):
            Anims3[i].y = player_y
        if player_y >= HEIGHT:
            player_y = 0
        animSpeed += 1
        if animSpeed % 20 == 0:
            animIndex += 1
            if animIndex >= numAnims:
                animIndex = 0
        last_player_y = player_y

pgzrun.go()