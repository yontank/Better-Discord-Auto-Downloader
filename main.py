import os
import re
import requests
import tempfile


def get_discord_path() -> tuple[str | bool]:
    discord_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Discord')
    # app-1.0.9208','modules', 'discord_desktop_core-1', 'discord_desktop_core', 'index.js

    if not os.path.exists(discord_path):
        return ("", False)

    regex_find_app_directory = re.compile(r'app-\d+\.\d+(\.\d+)?')

    dirs = os.listdir(discord_path)

    app_folder = list(filter(regex_find_app_directory.match, dirs))

    if len(app_folder) != 1:
        return ("", False)

    app_folder = app_folder[0]

    discord_path = os.path.join(discord_path, app_folder, 'modules',
                                'discord_desktop_core-1', 'discord_desktop_core', 'index.js')

    return (discord_path, True)


def get_bc_location(file: str) -> tuple[str, bool]:
    rx_get_better_discord_path = re.compile(r"^require\(\"(.*)\"\)\;$")

    with open(file, 'r') as f:
        for line in f:
            if ('betterdiscord.asar' in line) or ('BetterDiscord' in line):
                return re.match(rx_get_better_discord_path, line).group(1)


def download_bc():
    tmp = os.path(tempfile.gettempdir())

    if not os.path.exists(tmp):
        print('Err, Couldn\' set a temporary directory')

    # response = requests.get(download_url, allow_redirects=True)
    # print(tmp)
    # if response.status_code == 200:
    #     with open(tmp, 'wb') as output:
    #         output.write(response.content)


def main():
    discord_path = get_discord_path()
    print(discord_path)
    bc_path = get_bc_location(discord_path[0])

    print(bc_path)

    if (os.path.exists(bc_path)):
        print("Discord is connected to better discord!")


if __name__ == '__main__':
    main()
