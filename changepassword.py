import bcrypt
import json
import os
from cryptography.fernet import Fernet
import base64
from jsonenc import decryptjson

appdata_path = os.getenv('APPDATA')
app_folder = os.path.join(appdata_path, 'passlocker')
userjson = os.path.join(appdata_path, 'passlocker', 'data')


def change_MP(user, MP, NMP):
    NMP = NMP.encode()

    with open(userjson, 'r') as f:
        userlist = json.load(f)

    salt = (userlist[user]["salt"]).encode("utf-8")

    if userlist[user]["hashed_pass"].encode() == bcrypt.hashpw(MP.encode(), salt):
        data = decryptjson(user, MP)

        userlist[user]["hashed_pass"] = bcrypt.hashpw(
            NMP, salt).decode("utf-8")

        kdf_key = bcrypt.kdf(NMP, salt, 32, 100)
        fernet_key = base64.urlsafe_b64encode(kdf_key)
        # Create a Fernet object using the encoded key
        encryption_key = Fernet(fernet_key)

        # Encrypt the message
        data = json.dumps(data)
        encdata = encryption_key.encrypt(data.encode())
        encdata = encdata.decode('utf-8')
        userlist[user]["enc"] = encdata
        with open(userjson, 'w') as f:
            userlist = json.dump(userlist, f, indent=4)

        return True

    else:
        print("wrong password")


def change_user(old_user, new_user):
    with open(userjson, 'r') as f:
        userlist = json.load(f)
        if new_user not in userlist:
            userlist[new_user] = userlist.pop(old_user)
        else:
            return False

    with open(userjson, 'w') as f:
        userlist = json.dump(userlist, f, indent=4)
    return True
