import os
from turtle import down
import requests


def download_bc_asar_file(bc_path: str):
    download_url = 'https://betterdiscord.app/Download/betterdiscord.asar'
    # bc_path = os.path.join('C:', 'Users', 'Yontank', 'Desktop', 'hello.asar')

    if not os.path.exists(bc_path):
        print('Err, Couldn\'t set a temporary directory')
        return False

    response = requests.get(download_url, allow_redirects=True)

    if response.status_code == 200:
        with open(bc_path, 'wb') as output:
            output.write(response.content)
    return True


def create_bc_path():
    appdata = os.getenv('APPDATA')

    if (appdata is None or not os.path.exists(appdata)):
        raise Exception('System running isn\'t windows doesn\'t exist')

    path = os.path.join(appdata, 'BetterDiscord')
    if (os.path.exists(path)):
        return None

    os.mkdir(os.path.join(path))
    os.mkdir(os.path.join(path, 'data'))
    os.mkdir(os.path.join(path, 'plugins'))
    os.mkdir(os.path.join(path, 'themes'))

    if not download_bc_asar_file(os.path.join(path, 'data', 'betterdiscord.asar')):
        return None

    return os.path.join(path, 'data', 'betterdiscord.asar')
