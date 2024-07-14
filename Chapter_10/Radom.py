from pathlib import Path
import json

'''import random
str = ['a', 'b', 'c', 'd', '1','2','3','4','5','6','7','8','9','0']
str_1 = []
for i in range(1,5):
    str1 = random.choice(str)
    str_1.append(str1)
    print(str_1)
#join只能连接字符串，不能连接int类型的数字
champion_str = ''.join(str_1)
print(f"if you numbers are {champion_str}, you win the $!")
my_str = ''
n = 0
while my_str.lower() != champion_str.lower():
    str_2 = []
    for i in range(1,5):
        my_str = random.choice(str)
        str_2.append(my_str)
        n += 1
    my_str = ''.join(str_2)
print(f"you need {n} times can win champion!")


#第十章  文件
#Path就是一个类，指向一个文件，方便文件操作
#将指向的文件保存到path中
path = Path('pi_digits.txt')
#contents存储路径文件的内容，以字符串存储，若是int或是float则需要强制转换
#read结尾会打印一个空字符串，所以会多一行空行出来
contents = path.read_text().rstrip()
#去除空行  rstrip()用于删除字符串末尾的空白字符、空格、制表符、换行符等。
#contents = contents.rstrip()
print(contents)

#绝对路径和相对路径，相对路径是从当前程序的文件夹开始
#绝对路径是从根目录开始写  mac "/"  win "\"
#path = Path('/home/eric/data_files/text_files/filename.txt')


#读取各行
lines = contents.splitlines()
#调用splitlines()后，此时的lines存储了各行的信息，保存为列表
print(lines)
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    print(line)


#以上代码可以简写：
for line in contents.splitlines():
    print(line)


#pi_string = ''.join(lines)
print(pi_string)
print(len(pi_string))

#打印1万位的后五十位
path = Path('pi_million_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")



#10.1
from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text().rstrip()
print(contents)

my_string = ''
for line in contents.splitlines():
    my_string += line.rstrip()
    message = f"In Python you can {my_string}"

print(message)
message = message.replace('Python', 'Java')
print(message)
print(len(my_string))

#字符串替换函数不会改变原来的字符串，只是暂时改变，所以下面的代码不会成功替换字符串
msg = "Hello World!"
msg.replace('Hello', 'World')
print(msg)
#正确写法：改变后要确定让其变化
msg = msg.replace('Hello', 'World')
print(msg)


path = Path('programming.txt')
#python只能将字符串写入文件，若是写入int或float类型则需要先强制类型转化
path.write_text('I love shit')

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

#在调用write()函数写入时，若指定文件已存在，则write_text会把内容删除再将指定内容写入其中
path = Path('programming.txt')
path.write_text(contents)


#10.4
contents = ''
while True:
    msg = input("Please enter your name(Enter 'q' to exit): ")
    if msg == 'q':
        break
    #牛的，给每条信息进行一个换行
    contents += f"{msg}\n"
path = Path('guest.txt')
#用户创建.txt文件，自拟文件名666
#path = Path(f"{msg}.txt")
path.write_text(contents)


#异常 exception   traceback回溯回馈
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Please enter your first number: ")
    if first_number == 'q':
        break
    second_number = input("Please enter your second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

#处理文件
path = Path('guest.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file '{path}' does not exist!")
else:
    #split()函数可以让contents字符串生成一个列表
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
    

#10.6
while True:
    num_1 = input("Please enter your first number:(Enter 'q' to quit):  ")
    if num_1 == 'q':
        break
    num_2 = input("Please enter your second number:(Enter 'q' to quit):  ")
    if num_2 == 'q':
        break
    try:
        #try里面要放可能会出错误的代码，当代码任意一行出问题时则抛出异常，
        #所以是在try里写可能出错的代码，而不是在try里判断，有错误再去执行
        num_1 = int(num_1)
        num_2 = int(num_2)
        sum = num_1 + num_2
        print(f"{num_1} + {num_2} = {sum}")
    except ValueError:
        print("Please enter numbers only!")
'''


#操作多个文件
def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"Sorry, the file '{path}' does not exist!")
        #错误保持程序继续运行，忽略错误
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{path}' has about {num_words} words.")

filenames = ['guest.txt', 'programming.txt', 'abc.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

path = Path('learning_python.txt')
count_words(path)


def open_files(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #pass
        print(f"Sorry, the file '{path}' does not exist!")
    else:
        print(contents.rstrip())

filenames = ['cats.txt', 'dogs.txt', 'pigs.txt']
for filename in filenames:
    path = Path(filename)
    open_files(path)


#10.10 字符串匹配算法
line = "Row, row, row you boat"
print(line.count('row'))
print(line.lower().count('row'))

TengWangGeXu = Path("TengWangGeXu.txt")
contents = TengWangGeXu.read_text(encoding='utf-8').rstrip()
print(contents.lower().count('水'))


#数据共享
#保存数据  json字符串与其他语言交互 json.dump()存储   json.loads()读取
numbers = [2,3,4,5,6,7,8,9]
#指定将数值列表存储在哪个文件中，通常用.json存储json格式
path = Path('numbers.json')
#用json.dumps()接收实参，生成一个字符串，其实就是将json字符串转化为字符串
contents = json.dumps(numbers)
path.write_text(contents)

path = Path('numbers.json')
#json.loads() 读取number.json中的数据
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)


#保存和读取用户生成的数据，json存在就是解决程序在中断时数据不会被抹掉
username = input("Please enter your username: ")

path = Path('usernames.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")

#读取已保存的json字符串并输出
path = Path('usernames.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcom back, {username}!")


#重构  就是函数原本多个功能给他拆分出来，不让他执行那么多任务


