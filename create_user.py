import bcrypt
import json
import os

appdata_path = os.getenv('APPDATA')
app_folder = os.path.join(appdata_path, 'passlocker')
userjson = os.path.join(appdata_path, 'passlocker', 'data')


def createuser(username, MP):

    if not os.path.exists(app_folder):
        os.makedirs(app_folder)

    if os.path.exists(userjson):
        with open(userjson, 'r') as f:
            users = json.load(f)
    else:
        users = {}

    if username in users:
        print("already exist")
        return False

    else:
        MP = MP.encode()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(MP, salt)
        hashed_password = hashed_password.decode("utf-8")
        salt = salt.decode("utf-8")
        users[username] = {"hashed_pass": hashed_password, "salt": salt}
        with open(userjson, 'w') as f:
            json.dump(users, f, indent=4)
        return True


if __name__ == "__main__":
    createuser("ali", "ali")
