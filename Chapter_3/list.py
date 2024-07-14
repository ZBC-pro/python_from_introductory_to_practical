#第三章  列表
names = ['小明', '小陈', '傻逼']
greeting = '你好,'
print(names[2] + '不能赴约')
names[2] = '小绿'
print(greeting + names[0])
print(greeting + names[1])
print(greeting + names[2])

print('有了更大的餐桌')
names.insert(0,'小林')
#insert是插入前面或中间的任意位置
names.insert(2,'小粉')
#append是直接加在末尾，不需要位置
names.append('毒师')
print(greeting + names[0])
print(greeting + names[1])
print(greeting + names[2])
print(greeting + names[3])
print(greeting + names[4])
print(greeting + names[5])
#pop后元素就不在列表中了！！！即使是第0个元素
# motoche = ['abc', 'def', 'ghi', 'jkl']
# print(motoche)
#
# pop = motoche.pop(0)
# popped_motoche = motoche.pop()
# too_expensive = 'def'
# motoche.remove(too_expensive)
# print(motoche)
# print(f'\nA {too_expensive.title()} is too expensive for me.')
# print(popped_motoche)

#练习3.4
names = ['a', 'b', 'c', 'd']
for name in names:
    print(f'{name}您好，请您参加晚宴！')
for i in range(4):
    print(names[i])
#pop默认弹走最后一个！！也可以指明下标弹元素
leaf_men = names.pop()
names.append('e')
for name in names:
    print(f'{name}您好，请您参加晚宴！')

names.insert(0,'f')
names.insert(3,'g')
names.append('h')
for name in names:
    print(name)
print('今晚只能邀请两人参加晚宴')
#[f,a,b,g,c,d,h]
i = len(names)
while i > 2:
    str = names.pop(i-1)
    print(f'{str}对不起，您无法参加晚宴了')
    i -= 1
for name in names:
    print(f'{name}您好，请您参加晚宴！')
names.clear()
for name in names:
    print(name)

num = ['e', 'd', 'c', 'b', 'a']
#sort排序是不可逆的，数组会直接被修改
#num.sort()  reverse=Ture是反转数组的意思 sorted()是临时排序
# print(sorted(num))
# print(sorted(num, reverse=True))
# print(num)
# num.sort(reverse=True)
# print(num)
#反向打印列表 reverse是反转元素顺序，而不是反转字母顺序排列，并且是永久修改，但可以随时在调用返回
# num.reverse()
# print(num)
#习题3.8
# place = ['纽约', '上海', '拉萨', '杭州', '乌鲁木齐']
# print(place)
# #按字母排序
# print(sorted(place))
# print(place)
# place.reverse()
# print(place)
# place.reverse()
# print(place)
# place.sort()
# print(place)
# place.sort(reverse=True)
# print(place)
# print(len(place))

#打印第-1位则会从后往前打印最后一个元素
#print(num[-1])
#打印-8会报错，因为已经越界
#print(num[-8])

