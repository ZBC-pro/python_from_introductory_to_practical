#第四章  操作列表
pizza_list = ['香肠披萨', '芝士披萨', '榴莲披萨']
for pizza in pizza_list:
    print('我喜欢' + pizza)
    #变量写法
    print('我喜欢' + f'{pizza}')
print('我真的喜欢披萨')

#创建列表1~100w，并打印
numbers = []
for number in range(1,1000001):
    numbers.append(number)
#for number in numbers:
    #print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#range函数，打印1~5时，只会打印四个数，这就是编程语言减一的效果
#默认右边是小于5的
for value in range(1,5):
    print(value)
#只填一个数字默认0~那个数字
for value in range(5):
    print(value)

#list函数将循环数字转化为列表，即数组,也可以限制阶数
# num = list(range(1,5,2))
# print(num)
#range几乎可以创建任意数值的集合,打印1~11的平方值
squars = []
for value in range(1,12):
    squar = value ** 2
    squars.append(squar)
print(squars)

squars2 = []
for value in range(1,12):
    squars2.append(value ** 2)
print(squars2)

num = [1,2,3,4,5,6,7,8,9,0]
print(min(num))
print(max(num))
print(sum(num))

#列表推导式 简化代码行数 将for循环和创建新元素的代码合并成一行
#定义一个列表名，方括号里定义一个表达式表示生成要存储到列表里的值，value**2表示range中数的平方，此时for循环没有:
squares = [value ** 2 for value in range(1,11)]
print(squares)

# for num in nums:
#     print(f'{num}是字母',end='')
#python对缩进要求很高
#练习4.2
# pizzas = ['芝士', '小龙虾', '草莓', '奥里给']
# for pizza in pizzas:
#     print(f'I Like {pizza}')
# print('I really like pizza!')


#习题4.3 100w求和
# i = [value * 1 for value in range (1,1000000)]
# print(sum(i))

#奇数
# m = [value * 1 for value in range(1,21,2)]
# for i in m:
#     print(i,end=' ')

#打印3~30整除3的数
#expected an indented block after 'if' statement on line 401 此错误为缩进问题
#if 缩进错误
s = []
for n in range(3,32):
    if n % 3 == 0:
        s.append(n)
for n in s:
    print(n,end=' ')

print('\n')

#立方  立方推导式
n3 = [value ** 3 for value in range(1,11)]
for n in n3:
    print(n,end=' ')

print('\n')

#切片 返回指定范围的元素
players = ['德玛西亚', '奥拉夫', '凯隐', '无极剑圣', '提莫']
# print(players[0:3])
# print(players[3:])
# print(players[:3])
#-3 表示输出列表后三个元素
# print(players[-3:])

#遍历切片
for player in players[:4]:
    print(f'{player.title()}是LOL的一员')

#复制列表，将一个列表复制给一个新表
#如果是从player表复制，则打印新表输出为'无极剑圣'，因为在遍历时，player中最后一个
#遍历的就是无极剑圣
LOL_player = player[:]
LOL_players = players[:]
print(players)
print(LOL_player)
print(LOL_players)

#赋值会发生什么 : 赋值操作后，这两张表相当于同一张表，在对这两张表操作时，实际是对一张表操作。
CF_players = players
print(CF_players)
CF_players.append('zitai')
print(CF_players)
players.append('huli')
print(players)

#习题4.10
print(players[:3])
#这种写法是错误的，因为切片必须是整数切片，而(len(players)-1)/2返回的不是整数而是浮点数
#print(players[(len(players)-1)/2:(len(players)-1)/2 + 3])
print(players[1:4])
print(players[-3:])


cats = ['波斯猫', '加菲猫', '短毛', '英伦长毛', '土猫', '三色猫']
cats_pluse = cats[:]
cats_pluse.append('白猫')
for cat in cats_pluse:
    print(f'My favourite is cat {cat}')

#元组 元组与列表不同，不能被修改，不可变
#列表用[ ], 元组用圆括号（ ），元组中的元素是不能被修改的
dimensions = (200,50)
print(dimensions[0])
print(dimensions)

#无法被赋值
#dimensions[0] = 250
for dimensions in dimensions:
    print(dimensions,end=' ')
print('\n')
#修改元组只能重新定义并赋值
dimensions = (400,50)
print(dimensions)

foods = ('kfc', 'madlao', 'hualaishi')
for food in foods:
    print(f'My favourite is {food}')
foods = ('kfb', 'madxiao', 'hualaishi')
print(foods)

#PEP 8 — StyleGuide for Python Code python官网