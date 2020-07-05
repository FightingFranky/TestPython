import pgzrun 

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

def draw_hp_bar(PrinceHP):
    #画血条
    PrinceHP.isdead()
    HPBar = Rect((20, 20), (200, 33)) #血槽
    CurrentHPBar = Rect((20, 20), (200*PrinceHP.CurrentHP/PrinceHP.FullHP, 33)) #当前血量
    screen.draw.rect(HPBar, 'black')
    screen.draw.filled_rect(CurrentHPBar, 'black')
