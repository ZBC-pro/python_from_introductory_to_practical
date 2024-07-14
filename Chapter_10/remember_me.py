from pathlib import Path
import json

#新增函数，如果存储了用户名则返回，没有则返回空
def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("Enter your new username: ")
    userage = input("Enter your age: ")
    usercity = input("Enter your city: ")
    contents = path.read_text()
    path.write_text(contents)
    return username

def greet_user():
    path = Path('usernames.json')
    username = get_stored_username(path)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
