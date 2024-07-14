from pathlib import Path

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
'''

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



