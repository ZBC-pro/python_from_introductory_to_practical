from random import randint

class Die:
    def __init__(self, num_sides=6):
        #筛子有6面
        self.num_sides = num_sides

    def roll(self):
        #返回1~多少面的随机值
        return randint(1, self.num_sides)