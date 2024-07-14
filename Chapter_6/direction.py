#第六章 字典
user = {
    'username': 'ikun',
    'first_name': 'cai',
    'last_name': 'xukun',
}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# key 和 value 可以简写为k、v
for k, v in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# 不一定非是key和value做循环的值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 这里也可以是name、language
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# 遍历所有键
for name in favorite_languages.keys():
    print(name.title())
# 即使不说是字典的key也是默认遍历字典的key关键字，在后面加上key更容易理解
for name in favorite_languages:
    print(name.title())

# 用当前的键访问其关连的值
friends = ['phil', 'sarah']
for name in favorite_languages.keys():  # .keys就是指字典中的关键字：名字
    print(f"Hi {name.title()}!")
    if name in friends:
        # 从字典中提取出好友喜欢的语言并打印  在字典中，name的值就是喜欢的语言
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language}!")
    # 判断字典里有没有想要的关键字，判断陈立农是否在字典中，没有的话抛出异常
    if 'chenlinong' not in favorite_languages.keys():
        print("ChenLiNnong, please take you poll!")

# 顺序遍历字典中所有的键 sorted 函数
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll !")

# 遍历字典中所有的值
# 用for循环提取出字典中的每一个值赋给language，打印这些值
for language in favorite_languages.values():
    print(language.title())

print('\n')

# for循环的方法会打印出所有值，但现实中我们只需要有用的数值就够了
# 集合set，剔除重复项
for language in set(favorite_languages.values()):
    print(language.title())

# 练习6.4

rivers = {'nile': 'egypt',
          'yangzi': 'china',
          'zhujiang': 'china',
          }
for name, country in rivers.items():
    print(f"The {name.title()} runs through the {country.title()}.")
for name in rivers.keys():
    print(name.title())
for country in rivers.values():
    print(country.title())

# 嵌套，字典列表，字典每条只能存储一个外星人的记录，不能存取多个
# 字典+链表可以轻松解决  列表中存储字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'blue', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 自动生成外星人
aliens = []
# 创建多个不同颜色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 查看有多少外星人
print(f"Total number of aliens: {len(aliens)}")

# 将前三个外星⼈修改为⻩⾊、速度中等且值 10 分
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    # 将原本是黄色的外星人进阶为红色
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 字典中存储列表
# 顾客点的配料表存储在字典中，toppings关联的是一个列表，一个键关联多个值，直接上列表
pizaa = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese'],
         }
# 两个双引号之间可以进行缩紧，不换行，起连接作用
print(f"You ordered a {pizaa['crust']} -crust pizza."
      "with the following toppings:")
for topping in pizaa['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'jen': ['python', 'c'],
    'sarah': ['c++'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'javascript'],
}
# 将每个人喜欢的语言，也就是字典的值存储在languages中，要想打印出一个人喜欢多种语言，则需要遍历languages
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    print(len(languages))
    if len(languages) == 1:
        # 逻辑错误 错在并未定义language，else里面的language是通过for循环定义的，此时打印language.title则还是上一个人的最后一个喜欢的语言
        # print(f"\t{languages.title()}")   这么写打印出的第二人的喜欢的语言是c而不是c++
        print(f"\t{languages[0].title()}")
    else:
        for language in languages:
            print(f"\t{language.title()}")

# 字典嵌套字典
# 每个用户嵌入他的基本信息，基本信息用字典存储
users = {
    'cai': {
        'first_name': 'cai',
        'last_name': 'xukun',
        'location': 'Beijing',
    },
    'chen': {
        'first_name': 'chen',
        'last_name': 'linong',
        'location': 'Hangzhou',
    },
    'fan': {
        'first_name': 'fan',
        'last_name': 'chengcheng',
        'location': 'Shanghai',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']}{user_info['last_name']}"
    location = user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")

# 习题6.7
people = {'cai': {'first_name': 'cai',
                  'last_name': 'xukun',
                  'age': 18,
                  'city': 'Anhui',
                  },
          'chen': {'first_name': 'chen',
                   'last_name': 'linong',
                   'age': 10,
                   'city': 'Jiangsu',
                   },
          'fan': {'first_name': 'fan',
                  'last_name': 'chengcheng',
                  'age': 20,
                  'city': 'Zhejiang',
                  }
          }
for people_name, people_messages in people.items():
    full_name = f"{people_messages['first_name']}{people_messages['last_name']}"
    age = people_messages['age']
    city = people_messages['city']

    print(f"\nUsername: {people_name}")
    print(f"{full_name.title()}")
    print(f"\tAge:{age}")
    print(f"\tCity:{city}")

# 6.8
pet_0 = {'pinzhong': {'jiafei'}, 'zhuren': {'liufeng'}, }
pet_1 = {'pinzhong': {'bosi'}, 'zhuren': {'qiang'}, }
pet_2 = {'pinzhong': {'baimao'}, 'zhuren': {'zhao'}, }

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(pet)

# 6.9
favorite_place = {'cai': ['Beijing', 'Shanghai'],
                  'chen': ['Hangzhou', 'Shanghai'],
                  'fan': ['Zhujiang', 'Shenzhen'],
                  }
for name, locations in favorite_place.items():
    print(f"\n{name}'s favorite place are:")
    for location in locations:
        print(f"\t{location}")

#6.10
favorite_numbers = {'cai': [1,3,5,7,9],
                    'chen': [2,4,6,8,10],
                    'fan': [3,5,6,7,8],
                    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    print(numbers)
    for number in numbers:
        print(f"{number}",end=" ")
print("\n")

#6.11
cities = {'Hangzhou': {'country': 'China',
                       'populations': 14000000,
                       'fact': 'very beautiful',
                      },
          'Xinjiang': {'country': 'China',
                       'populations': 340000,
                       'fact': 'very amazing',
                      },
          'Beijing': {'country': 'China',
                       'populations': 109000990,
                       'fact': 'center in China',
                      },
          }

for name,cities in cities.items():
    print(f"{name}:",end="")
    country = cities['country']
    populations = cities['populations']
    facts = cities['fact']
    print(f"from {country},have populations:{populations}, and it had facts:{facts}")

friend = {"first_name": "小明", "last_name": "朱", "age": 25,
          "city": "深圳"}
print("姓名:" + friend["last_name"] + friend['first_name'])
print("年龄:" + str(friend["age"]))
print("城市:" + friend["city"])

#遍历字典
temperature_dict = {"001": 36.4, "002": 36.6, "003": 38.8, "004": 40.9}
for temperature_tuple in temperature_dict.items():
    staff_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if temperature >= 38:
        print(staff_id)

        #键key : 值value
rivers = {"Nile": "Egypt", "Yangze River": "China", "Amazon River": "Brazil"}
for river, country in rivers.items():
    print("The " + river + " runs through " + country + ".")
for river in rivers.items():
    print(river)
for river in rivers.keys():
    print(river)
for country in rivers.keys():
    print(country)
for country in rivers.values():
    print(country)

# 格式化字符串 1.format,{}替换值，类似于JS代码
# 三种发信息的方式：
# demo1
# contacts = ["老余", "老林", "老李", "老张", "老曾"]
# for name in contacts:
#     message_contacts = name + ": 新年快乐！" + name + "虎年大吉！"
#     print(message_contacts)
# # format解决频繁使用 + 导致的不美观
# message_contact = '''
# 率会出暖，心愿朝气。
# 心碎朴志，夫妻东来。
# 金{0}贺门，换了祥瑞。
# 金{0}敲门，五福临门。
# 给{1}拜年了！
# 新船快啊了，{0}年妲己！
# '''.format("虎", "老林")
# print(message_contact)
#
# message_contact = '''
# 率会出暖，心愿朝气。
# 心碎朴志，夫妻东来。
# 金{current_year}贺门，换了祥瑞。
# 金{current_year}敲门，五福临门。
# 给{receiver_name}拜年了！
# 新船快啊了，{current_year}年妲己！
# '''.format(current_year="虎",
#            receiver_name="老林")
# print(message_contact)
#
# name = "老林"
# year = "龙"
# message_contact = f'''
# 率会出暖，心愿朝气。
# 心碎朴志，夫妻东来。
# 金{year}贺门，换了祥瑞。
# 金{year}敲门，五福临门。
# 给{name}拜年了！
# 新船快啊了，{year}年妲己！
# '''
# print(message_contact)
#
# gpa_dict = {"小明": 3.251, "小花": 3.896, "小兰": 3.996, "小李": 2.622,
#             "小强": 3.999}
# for name, gpa in gpa_dict.items():
#     # {1:1f}小数点后保存一位小数。
#     print("{0}你好，你的当前GPA为:{1:.1f}".format(name, gpa))
#