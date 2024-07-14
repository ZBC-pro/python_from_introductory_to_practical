import math


#第二章
print(math.log2(8))
str = 'Hello'[3]
str1 = 'hello'
print(str)
print(len(str))
#打印字符串的最后一个字符的两种方法
print(str1[4])
print(str1[len(str1)-1])

a1 = True
a2 = False

#type函数是识别出该函数的类型
print(type(str1))
print(type(1.5))

my_favorite_language = 'Python'
message = "Hello {}!".format(my_favorite_language)
messa = f"hello {my_favorite_language}"
print(messa)
print(message)