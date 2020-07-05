#### 需引入全局变量 standard_speed
standard_speed = 2


####下方代码替换原怪兽自走模块

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