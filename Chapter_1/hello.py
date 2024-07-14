import math
#import this

#第一章
#.tittle 首字母大写
name = "add lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
full_name = f"{first_name}{last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython")
print("\n\tPython")

favorite_language = " Python "
print(favorite_language.rsplit())
print(favorite_language.lstrip())
print(favorite_language.strip())

nostarch_url = 'https://www.google.com'
a= nostarch_url.removeprefix('https://')
print(a)
print("\n\n\n\n\n\n")

Eric = "Hello Eric,would you like to learn some Python?"
a = Eric
print(a)
print(a.lower())
print(a.upper())
print(a.title())

mao = 'Alber,"a person"'
print(mao)

filename = 'python_note.txt'
print(filename.removesuffix('.txt'))

#开头加f表示字符串被赋值，不带f表示没被赋值
name = Eric.upper()
print(f'Hello {name},would you like to learn some Python?')