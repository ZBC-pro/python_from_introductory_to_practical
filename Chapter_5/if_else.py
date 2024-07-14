#第五章 ! >> && >> ||
alien_color = 'red'
if alien_color == 'green':
    print('you got five point')
elif alien_color == 'yellow':
    print('you got ten point')
else:
    print('you got twenty points')

request_topping = 'mushroom'
if request_topping != 'mushrooms':
    print('Sorry, you are not mushroom.')

#查找特定的值是否在列表内，后期在数据库登陆时用得到
user = ['e', 'd', 'c', 'b', 'a']
if 'a' in user:
    print('yes')

banners = ['shit', 'fuck', 'sb']
ask = 'fuc'
if ask not in banners:
    print(f'{ask.title()} this ask is a treeible ask!')

#习题5.1条件预测
print(1 > 2)
print('a' == 'b')
#字符串不能直接和数值比较，会直接判定错误
print('a' == 97)
#要想‘a’ 与 97进行比较，则要么a转化成int型，要么97转化为字符串
# ord() 函数是 Python 中的一个内置函数，字符串中指定字符的 Unicode 值
print(ord('a') == 97)
#97转化为字符串不是‘a'
print(str(97) == 'a')  #false

print(1==1 and 2==2)
print(1==1 or 3==2)

#习题5.3
alien_color = 'red'
if alien_color == 'red':
    print('you got 5 point')
if alien_color != 'green':
    print('you got ten point')

if alien_color == 'green':
    print('you got five point')
elif alien_color == 'yellow':
    print('you got ten point')
else: print('you got twenty points')

age = 66
if age < 2:
    print('you are a baby')
elif age < 4:
    print('you are a child')
elif age < 13:
    print('you are a teenager')
elif age < 18:
    print('you are a youther')
elif age < 65:
    print('you are a man')
else: print('you are a older')

furits = ['apple', 'orange', 'pear']
for furit in furits:
    if furit == 'apple':
        print('you really like apple')
    if furit == 'orange':
        print('you really like orange')
    if furit == 'pear':
        print('you really like pear')

available_toppings = ['mushrooms', 'tomatos','green peppers', 'e',
                      'apple', 'banana']
request_toppings = ['mushrooms', 'tomatos', 'green peppers', 'e']

for request_topping in request_toppings:
    print(request_topping,end=' ')
    if request_topping in available_toppings:
        print(f'Adding {request_topping.title()} successfully!')
    else:
        print(f'Sorry, {request_topping.title()} not enough!!')
print('finish')

admins = ['admin','ab']

users = ['liming', 'john']

for admin in admins:
    if admin in admins:
        print(f'is {admin}')
