import pgzrun
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



def draw():
    global t
    screen.fill('gray')
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