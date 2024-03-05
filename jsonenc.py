import bcrypt
from cryptography.fernet import Fernet
import base64
import json
import os

appdata_path = os.getenv('APPDATA')
userjson = os.path.join(appdata_path, 'passlocker', 'data')
app_folder = os.path.join(appdata_path, 'passlocker')


def encryptjson(original, user, MP):
    original = json.dumps(original)
    MP = MP.encode()
    with open(userjson, 'r') as f:
        users = json.load(f)
        salt = users[user]["salt"].encode()
    kdf_key = bcrypt.kdf(MP, salt, 32, 100)

    fernet_key = base64.urlsafe_b64encode(kdf_key)
    fernet = Fernet(fernet_key)
    # encrypting the file
    encrypted = fernet.encrypt((original).encode())

    users[user]["enc"] = encrypted.decode()
    with open(userjson, 'w') as f:
        json.dump(users, f, indent=4)


def decryptjson(user, MP):

    with open(userjson, 'r') as f:
        users = json.load(f)
        salt = users[user]["salt"].encode()

    MP = MP.encode()
    kdf_key = bcrypt.kdf(MP, salt, 32, 100)
    fernet_key = base64.urlsafe_b64encode(kdf_key)
    fernet = Fernet(fernet_key)
    try:
        userdata = users[user]["enc"]
        decrypted = (fernet.decrypt(userdata)).decode()
        decrypted = json.loads(decrypted)
    except:
        return {}
    return decrypted
