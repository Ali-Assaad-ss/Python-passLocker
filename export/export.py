from tkinter import filedialog
import json
import os

appdata_path = os.getenv('APPDATA')
app_folder = os.path.join(appdata_path, 'passlocker')
userjson = os.path.join(appdata_path, 'passlocker', 'data')


def export(user):
    with open(userjson, 'r') as f:
        users = json.load(f)

    backupdata = users[user]

    download_location = filedialog.askdirectory(
        title="Select Download Location"
    )

    if download_location:
        with open(download_location+"/backup.json", "w")as f:
            json.dump(backupdata, f, indent=4)
        return True
    else:
        return False
