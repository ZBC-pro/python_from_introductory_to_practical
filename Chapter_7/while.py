#第七章 while循环人机交互
message = input("Tell me something, and I will repeat it back to you:")
print(message)

#多行提示操作：
prompt = "If you share you name, we can personalize the messages you see."
prompt += "\nWhat is your name?"

name = input(prompt)
print(f"\nHello {name}")

#年龄虽然输入的是数字，但是在python中则是以字符串的方式输入的，输入21后只能作为字符串‘21’看待，不能用作数值运算
age = input("How old are you?")
#或者可以直接转化
#age = int(input("How old are you?"))
#需要强制类型转换才能和数值相比较
int(age) <= 18
print(age)

hight = int(input("How tall are you, in inches?"))
if hight >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("You are a little too tall.")

#7.3
cars = input("What kind of you want dirve car?")
print(f"Let me see if I can find you a {cars}.")

num = int(input("How numbers coming? "))
if num >= 8:
    print("No tables.")
else:
    print("Coming.")

num = int(input("Enter a number: "))
if num%10 ==0:
    print("Y")
else:
    print("N")

#while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#条件退出循环
prompt = "while循环"
#必须给变量 message 指定初始值,否则message没有初始值无法进入while循环
message = ""
while message != 'quit':
    message = input(prompt)
    #消除最后一次循环时多打印出的quit提示
    if message != 'quit':
        print(message)


#为while循环创立结束flag
flag = True
while flag:
    message = input()
    if message == 'quit':
        #或者使用break去退出循环
        #break
        flag = False
    else:
        print(message)

#continue的用法 打印奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#while每循环一次都要给num重新赋值，不然会陷入死循环，因为num的值从未变化，就是你第一次输入的值
num = int(input("Enter you age: "))
while num > 0 and num < 120:
    if num < 3:
        print("free")
        num = int(input("Enter you age: "))
    elif num < 12:
        print("10$")
        num = int(input("Enter you age: "))
    else:
        print("15$")
        num = int(input("Enter you age: "))

#while处理字典  验证用户
#先创建一个待验证的用户表和一个用于存储已验证用户的空表
unconfirmed_users = ['cai', 'chen', 'fan',]
confirmed_users = []

#验证每个用户，直到没有未验证的，并且将验证后的用户移入已验证的标中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users are confirmed:")
for user in confirmed_users:
    print(user.title())


#删除列表中的特定值，一个元素出现多次，可以利用while删除
pets = ['dog', 'cat', 'mouse', 'rabbit', 'cat', 'cat', 'cat']
print(pets)

#remove只能删除一个,自己定位或者默认最前面的那个，遍历寻找时最先找到的那个
pets.remove('cat')
print(pets)

#可以理解为当pets列表中有‘cat’时
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#用户输入填充字典
responses = {}
#设置一个标志，判断是否继续输入
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    #将答案存储在字典中
    #这里的字典存储方法是字典中存储字典，先输入姓名，然后姓名对应你的回应response
    #response对应一条，去爬哪座山,其中，name是外层字典的key键，value值是字典response
    #response值将存储在以name为键的字典中
    #其中，mountain是键，input输入的是值,抽象化就是下面这样
    # {
    #     'cai': {'mountain': 'taishan'，
    #             },
    # }
    responses[name] = response

    #判断是否还有人参与
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---\n")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")

#习题7.8
sandwich_orders = ['zhishisandwich', 'malasandwich', 'jiaotangsandwich',
                   'zhishisandwich' ,'zhishisandwich', 'zhishisandwich',
                   ]
print("zhishisandwich is saled out!")
while 'zhishisandwich' in sandwich_orders:
    sandwich_orders.remove('zhishisandwich')

finished_sandwiches = []
while sandwich_orders:
    name = sandwich_orders.pop()
    print(f"{name} is be done sandwich.")
    finished_sandwiches.append(name)
for sandwich in finished_sandwiches:
    print(sandwich)


#7.10 综合自创题目，存储每个人喜欢的城市，一个键值对应一个链表并结合前面的案例输出并判断链表是否为单个值
User_dream_places = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    #知道字典中name对应一个链表，但是不能直接想当然的用，还要先定义一个空链表，在尾部追加
    dream_place = []
    flag = True
    #一个人可以选择多个地方，字典中name键对应一个列表为值
    while flag:
        response = input("\nWhat is your dream places? ")
        dream_place.append(response)
        repeat = input("Would you like to let another place? (yes/no)")
        if repeat.lower() == 'no':
            flag = False

    # {
    #     name:[dream_place],
    # }
    User_dream_places[name] = dream_place

    ask = input("Another person respond?(yes/no)")
    if ask.lower() == 'no':
        polling_active = False

for name,dream_places in User_dream_places.items():
    print(f"\n{name.title()} would like to:")
    if len(dream_places) == 1:
        print("\t",dream_places[0].title())
    else:
        for place in dream_places:
            print("\t",place.title(),end=' ')

#bilibili
user_age = int(input("请输入您的年龄:"))
user_age_after_10_years = user_age + 10
print("您十年后是" + str(user_age_after_10_years)  + "岁")


number = int(input("请输入一个数字:"))
if number % 10 == 0:
    print("您输入的数是十的倍数！\n")
list1 = ['你', '好', '吗', '兄', '弟']
for char in list1:
    print(char,end='')
for i in range(len(list1)):
    print(list1[i],end='')
i = 0
while i < len(list1):
    print(list1[i],end='')
    i += 1
user_input = input('请输入你想要添加的配料:')
while user_input != 'quit':
    print('好的，披萨里会添加' + user_input)
    user_input = input('请输入你想要添加的配料:')
