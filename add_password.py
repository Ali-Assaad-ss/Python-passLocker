from cryptography.fernet import Fernet
from jsonenc import encryptjson, decryptjson


def addtojson(type, Muser, MP, website, User, password, note=""):
    data = decryptjson(Muser, MP)

    if type == "pass":
        entries = {"website": website, "username": User,
                   "password": password, "note": note}
    if type == "auth":
        entries = {"website": website, "username": User, "authkey": password}

    label = "authacc" if type == "auth" else "accounts"

    if label in data:
        data[label].append(entries)
    else:
        data[label] = []
        data[label].append(entries)
    encryptjson(data, Muser, MP)
