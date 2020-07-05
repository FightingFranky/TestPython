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