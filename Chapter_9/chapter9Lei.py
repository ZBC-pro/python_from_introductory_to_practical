'''
#第九章 面向对象
#面向过程 == 编写函数
#面向对象 == 模拟现实物品，定义ATM类，类似于数据结构链表
#方法就是放在类里的函数，属性就是放在类里面的变量
#面向过程是编年体，面向对象是纪传体，一个是按时间记录，一个是按人物故事去记录
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        print(f"{self.name} rolled over.")

cat1 = CuteCat('JiaFei',2,'绿色')
print(f'{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}')

# 书写规范：例如for cat in cats：
# for dog in dogs，单个物品在一个集体里循环

#第九章 类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is nowing sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over!")

my_dog = Dog("Jack", 2)
your_dog = Dog("Pop", 3)

print(f"My dog name is {my_dog.name}.")
print(f"My dog age is {my_dog.age}.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog name is {my_dog.name}.")
print(f"Your dog age is {my_dog.age}.")
your_dog.sit()
your_dog.roll_over()


#习题9.1.4.6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name.title()}, occur food is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"The restaurant name is oping now!.")

    #打印就餐人数
    def read_number_served(self):
        print(f"The restaurant own {self.number_served} guests.")

    #修改就餐人数
    def set_number_served(self, number):
        if number > self.number_served:
            self.number_served = number
        else:
            print("You can't roll back guest numbers!")

    #设置就餐人数自增
    def increment_number_served(self, number):
        if number < 0:
            print("You can't roll back guest numbers!")
        else:
            self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = ['奶油', '香草', '可乐', '哈根达斯']

    def decribe_flavor(self):
        print("\n冰淇凌的口味有：")
        for flavor in self.flavor:
            print(flavor,end=' ')

    #每次只能传一个参数，可以升级为传一个列表
    def insert_flavor(self, Ice_type):
        if Ice_type is not None:
            if len(Ice_type) > 1:
                for flavor in Ice_type:
                    self.flavor.append(flavor)
            else:
                self.flavor.append(Ice_type)
        else:
            print("You can't inseret nothing things!")


restaurant = Restaurant("meihua", "china")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("xuehua", "usa")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant("guihua", "china")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant("fanghua", "japan")
restaurant_3.read_number_served()

print("\n")
restaurant_3.set_number_served(5)
restaurant_3.read_number_served()
restaurant_3.set_number_served(3)
restaurant_3.read_number_served()

print("\n")
restaurant_3.increment_number_served(2)
restaurant_3.read_number_served()
restaurant_3.increment_number_served(-1)
restaurant_3.read_number_served()

print("\n")
restaurant_4 = IceCreamStand("yijia", "france")
restaurant_4.decribe_flavor()

restaurant_4.insert_flavor('苹果')
restaurant_4.decribe_flavor()

type = ['梨', '香蕉', '菠萝', '荔枝']
restaurant_4.insert_flavor(type)
restaurant_4.decribe_flavor()



#习题9.4.8
class User:
    def __init__(self, first_name, last_name, age, hobbies):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobbies = hobbies
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nname:{self.first_name} {self.last_name}, age:{self.age}, hobbies:{self.hobbies}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, how may I help you?")

    def login_lock_print(self):
        print(f"You login_attempt is {self.login_attempts}.")

    def increment_login_attempts(self):
        if self.login_attempts == 0:
            self.login_attempts = 1
        else:
            print("Your already logged in!")

    def reset_login_attempts(self):
        if self.login_attempts == 1:
            self.login_attempts = 0
        else:
            print("Your already reset!")


class Admin(User):
    def __init__(self, first_name, last_name, age, hobbies):
        super().__init__(first_name,last_name,age,hobbies)
        self.privileges = Privileges()

class Privileges:
    #只定义一个列表，不传参
    def __init__(self):
        self.privileges = ["can addpost", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nAdmin 拥有的权限有:")
        #去掉末尾的，方法1:join()字符串拼接函数
        print(', '.join(self.privileges))
        #法2: 条件判断法
        # i = 0
        # for privilege in self.privileges:
        #     if i == len(self.privileges) - 1:
        #         print(privilege)
        #     else:
        #         print(privilege, end=',')
        #     i += 1



user_1 = User("cai", "xukun", "18", ["sing", "jump", "rap"])
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.login_lock_print()

user_1.reset_login_attempts()
user_1.login_lock_print()

user_1.reset_login_attempts()
user_1.login_lock_print()

#子类自创的权限只能子类去调用，但子类仍可以调用父类
admin_1 = Admin("chen", "linong", "22", ["sing", "jump", "rap", "basketball"])
admin_1.privileges.show_privileges()
print("\n")
admin_1.increment_login_attempts()
admin_1.login_lock_print()

admin_1.privileges.show_privileges()
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    #通过方法修改属性的值
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    #通过方法让属性值递增  接收一个英里数并追加到odometer_reading中
    def increment_odometer(self, miles):
        if miles < 0:
            print("增长数不能为负")
        else:
            self.odometer_reading += miles

my_new_car = Car("Ford", "BMW", "2024")
print("\n")
print(my_new_car.get_discriptive_name())
my_new_car.read_odometer()

#修改属性值  1.直接修改 笨拙，一般都是程序帮你修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#2.通过方法修改  将update_odometer()方法写入Car类中
# def update_odometer(self, mileage):
#     self.odometer_reading = mileage
my_new_car.update_odometer(500)
my_new_car.update_odometer(10)
my_new_car.read_odometer()

#通过方法让属性值递增
print("\n")
my_used_car = Car("redbull", "bzen", "2023")
print(my_used_car.get_discriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


#组合  将大类拆分为小类
# 面向对象编程时，类、方法越来越多，文件越来越长，比如电动车里的一些类，当你在给电车添加功能时，
# 有很多类都是针对电池的属性或方法，这时就可以将这写单拿出来作为一个电池类,电车要用这个类一定要写在电车类前面
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


my_leaf = ElectricCar("china", "BYD", "2024")
print("\n")
print(my_leaf.get_discriptive_name())
my_leaf.battery.decribe_battery()
my_leaf.battery.get_range()

print("\n")
my_leaf_1 = ElectricCar("usa", "tsl", "2023")
print(my_leaf_1.get_discriptive_name())
my_leaf_1.battery.get_range()
my_leaf_1.battery.upgrade_battery()
my_leaf_1.battery.get_range()


#python标准库，可以调用python的各种库和类
print("\n")#随机数和名
from random import randint
print(randint(1,6))

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

#习题9.13
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

Six_sided_dice = Die()
print(Six_sided_dice.roll_die())

Ten_sided_dice = Die(10)
j = 0
for i in range (1,11):
    #这么写是错误的，因为jion必须是返回一个列表或者元组，如果是一个一个的返回，则会出现类型错误
    #print(','.join(Ten_sided_dice.roll_die()))
    if j == 9:
        print(Ten_sided_dice.roll_die())
    else:
        print(Ten_sided_dice.roll_die(),end=',')
    j += 1


#9.14.15
str = ['5','8','9','4','3','a','c','l','m','c']
str1 = []
for i in range(1,5):
    string = choice(str)
    str1.append(string)
    print(str1)
str2 = ''.join(str1)
print(str2)
print(f"if you numbers was {str2}, you win the champion!")
my_str = ''
n = 0
while str2.casefold() != my_str.casefold():
    my_ticket = []
    for i in range(1,5):
        my_string = choice(str)
        my_ticket.append(my_string)
    my_str = ''.join(my_ticket)
    n += 1
print(f"需要{n}次才能中奖！")


#Python 3 Module of the Week　python标准库，探索其中的模块
#类使用的是驼峰法编程






