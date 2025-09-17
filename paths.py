import os
import re
import requests
import tempfile

#   The code checks if the discord path contains a specific file, which better discord injects itself into,
#   if the file exists, we will return is path, otherwise we will return None.


def get_discord_path() -> str | None:
    sep_1 = os.getenv('LOCALAPPDATA')

    if sep_1 is None:
        return None

    discord_path = os.path.join(sep_1, 'Discord')

    if not os.path.exists(discord_path):
        return None

    regex_find_app_directory = re.compile(r'app-\d+\.\d+(\.\d+)?')

    dirs = os.listdir(discord_path)

    app_folder = list(filter(regex_find_app_directory.match, dirs))

    if len(app_folder) != 1:
        return None

    app_folder = app_folder[0]

    discord_path = os.path.join(discord_path, app_folder, 'modules',
                                'discord_desktop_core-1', 'discord_desktop_core', 'index.js')

    if (not os.path.exists(discord_path)):
        return None

    return discord_path


def get_bc_asar_location(file: str) -> str | None:
    rx_get_better_discord_path = re.compile(r"^require\(\"(.*)\"\)\;$")

    with open(file, 'r') as f:
        for line in f:
            if ('betterdiscord.asar' in line) or ('BetterDiscord' in line):
                val = re.match(rx_get_better_discord_path, line)

                if val is None:
                    return None

                val = val.group(1)
                return val


def get_bc_location() -> str | None:
    pass


def main():
    discord_path = get_discord_path()
    
    if not discord_path:
        raise Exception("Didn't Find discord path.")

    bc_path = get_bc_asar_location(discord_path)

    if bc_path is None:
        raise Exception("Couldn't Find Better Discord Folder")

    print(bc_path)
    if (os.path.exists(bc_path)):
        print("Discord is connected to better discord!")


if __name__ == '__main__':
    main()
