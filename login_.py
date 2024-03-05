import bcrypt
import json
import os
appdata_path = os.getenv('APPDATA')
userjson = os.path.join(appdata_path, 'passlocker', 'data')
app_folder = os.path.join(appdata_path, 'passlocker')


def login(user, pass_input):
    if not os.path.exists(app_folder):
        os.makedirs(app_folder)

    if os.path.exists(userjson):
        with open(userjson, 'r') as f:
            users = json.load(f)
    else:
        users = {}

    if user in users:
        pass_input = pass_input.encode("utf-8")
        salt = (users[user]["salt"]).encode("utf-8")
        hashed_pass_input = (bcrypt.hashpw(pass_input, salt)).decode("utf-8")
        hashed_pass = users[user]["hashed_pass"]
        if hashed_pass == hashed_pass_input:
            return user, pass_input
    else:
        print("login failed")
    return False, False
