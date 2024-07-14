'''
#第八章 函数
#实参和形参,def函数 括号中的是形参，调用函数时是实际参数
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('jhon')


def favorite_book(book):
    print(f"One of my favorite books is {book.title()}")

favorite_book('War Or Peace')

#函数传递可以是多个形参，并且传递时可以是位置实参、关键字实参、字典、列表都可以
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('jiafei', 'jhon')
describe_pet('dog', 'joon')

#关键字实参，即使是位置错误，最终结果也不会错
describe_pet(pet_name='hj', animal_type='pig')

#默认值一般在定义函数时，在形参里定义如，并且将有默认值的放后面，没默认值的放前面，这是必须的
# 错误写法 默认值在前面会报错 def describe_pet_1(animal_type = 'dog',pet_name):
def describe_pet_1(pet_name,animal_type = 'dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_1('while')

#返回值
#添加额外的中间值，并非所有人都有中间名，所以要加判断
def get_formatted_name(first_name, last_name, middle_name = ''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

#middle_name 只能定义在最后面，因为有些人可能没有中间名
musician = get_formatted_name('jhon',  'lsg')
musician = get_formatted_name('cai',  'xu', 'kun')
print(musician)


#定义一个创建字典的函数，并返回字典
def build_person(first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name}
    #判断有没有age，有的话自动添加到字典，没有的话就默认为None
    if age:
        person['age'] = age
    return person

musician = build_person('abc', 'def', age = 18)
print(musician)


#无限输入的统计表用户表
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


#习题8.6
def city_country(name,belong_nation):
    full_name = f"{name}, {belong_nation}"
    return full_name.title()

while True:
    city_name = input("\nPlease input your city name:")
    if city_name == 'q':
        break
    city_belong_nation = input("\nPlease input your city belong nation:")
    if city_belong_nation == 'q':
        break

    city = city_country(city_name,city_belong_nation)
    print(city)

#8.7~8
def make_album(singer, work, num = None):
    full_name = f"歌手：{singer} 代表作：{work} 知名作品数量：{num}"
    return full_name.title()

while True:
    singer_name = input("\nPlease input your name:")
    if singer_name == 'q':
        break
    work_name = input("\nPlease input your work:")
    if work_name == 'q':
        break
    sings_number = int(input("\nPlease input your sings number:"))
    if sings_number == 'q':
        break

    test = make_album(singer_name,work_name,sings_number)
    print(test)


#传递列表,在函数中对这个列表所做的任何修改都是永久的!!!C语言还要取地址，很麻烦
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['cai', 'chen', 'fan', ]
greet_users(usernames)


#前一章的验证用户问题，一个列表中的用户验证后都写入另一个列表中，不用函数的写法；
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
#
# while unprinted_designs:
#  current_design = unprinted_designs.pop()
#  print(f"Printing model: {current_design}")
#  completed_models.append(current_design)
#
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#  print(completed_model)

#用函数改写此功能
 # IndentationError: unexpected indent 此错误一般为缩进错误，缩进错误：意外的缩进
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)


#不修改传进函数的列表的值---存一个列表副本
#function_name(list_name[:])
#此时使用的是列表的副本，不改变定义的列表，函数依然执行
print_models(unprinted_designs[:], completed_models)
show_completed_models(unprinted_designs)
show_completed_models(completed_models)


#习题8.9
message_list = ['cai', 'chen', 'fan', 'huang', ]
associate_messages_list = []

def show_messages(message_list):
    print("\nThe following messages have been printed:")
    for message in message_list:
        print(message,end=' ')

#在 Python 中，函数的参数类型是可选的，这意味着你不需要指定它们的具体类型。
#当你定义一个函数时，你可以使用任何你喜欢的变量名作为参数，
# Python 会在运行时根据实际传递的值来确定这些参数的类型，所以随便你命名，只要名称能对应的上就行
def send_massages(message_list, associate_messages_list):
    while message_list:
        msg = message_list.pop()
        print(f"短文：‘{msg}’已保存为副本。")
        associate_messages_list.append(msg)

#send_massages(message_list, associate_messages_list)
#函数调用时的实参可以和函数定义时的形参名称不同，只要是一个list类型就行。
send_massages(message_list[:], associate_messages_list)
show_messages(message_list)
show_messages(associate_messages_list)


# *加上形参python可以直接识别出你有几个实参,无论多少值，都能打印出来
#原理：python会收集到一个形参的size，然后再创建一个元祖填入其中
#在C语言中则是（argc，*argvs），一个是传个数，一个是传参数，一般参数个数对应你所输入的个数
#*args则是收集n多个实参
def make_pizaza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizaza(16,'tomato')
make_pizaza(24,'mashrooms', 'green pepers', 'extra cheese')





# **user_info是创建一个名为user_info的字典，存储函数收到的名值对，与其他字典相同可以访问修改。
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

user_profile_1 = build_profile('jhon', 'joyzhi',
                               location='beijing',
                               field='mathmatics')

print(user_profile)
print(user_profile_1)


def make_sandwich(*toppings):
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('qingcai', 'mogu', 'baicai', 'aoerliangjirou')


def car_messages(manufacturer, type, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["type"] = type
    return car_info

car = car_messages('dazhong', 'aodi', color = 'blue', piece = 430000)
print(car)


#导入特定函数
from pizza import make_pizaza
import pizza

pizza.make_pizaza(34,'mushroom')

#给指定函数另起别名
from pizza import make_pizaza as mp

mp(99,'a', 'b')

#给指定模块起别名
import pizza as p

p.make_pizaza(90,'d')

#导入模块中的所有函数
from pizza import *


#第八章tips
#在给形参指定默认值时，等号两边不要有空格：调用时等号两边也不要有空格
#def function_name(parameter_0, parameter_1='default value')
#function_name(value_0, parameter_1='value')


#第八章 函数_bilibili
# def calculate_sector(center_angle, radius):
#     sector_area = center_angle / 360 * 3.14 * radius ** 2
#     print(f'此扇形的面积为:{sector_area}')
#     return sector_area  #有了return就给了可以再次操作这个数的机会！！
#
# sector_area_1 = calculate_sector(180,3)
#
# def favorite_book(title):
#     print('my favorite book is {}'.format(title))
#     print(f'my favorite book is {title}')
# favorite_book('B&C')
#
# def city_country(city, country):
#     return f'{city}, {country}'
#
# #有返回值才能打印
# print(city_country('杭州','中国'))
'''