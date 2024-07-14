#因为电车类需要继承父类，但此模块只存储电车类，所以要先把父类导入进来
from car import Car

class Bettery:
    def __init__(self, battery_size=40):
        # 初始的电池尺寸属性
        self.battery_size = battery_size

    def decribe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        #获取电车里程
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


#继承  汽车——---电动汽车
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # 初始化父类属性   super()函数可以让你调用父类的方法，父类又称为超类，所以是super，并且一定要加括号
        super().__init__(make, model, year)
        self.battery = Bettery()

    #子类定义属性  父类不需要，专属子类时，重写让父类忽略此方法
    #假设父类有fill_gas_tank()的方法，在子类中不需要，可以对其进行重写，调用子类时会抛出异常
    #有人对电动车调用fill_gas_tank()方法时就会报错。可以从父类取其精华，去其糟粕
    def fill_gas_tank(self):
        print("This car doesn't has a gas tank!")