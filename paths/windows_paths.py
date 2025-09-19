import os
import re
import requests
import tempfile
from abstract.abstract_paths import AbstractPaths
#   The code checks if the discord path contains a specific file, which better discord injects itself into,
#   if the file exists, we will return is path, otherwise we will return None.


class WindowsPaths(AbstractPaths):
    def get_discord_path(self) -> str | None:
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

    def get_bc_path(self) -> str | None:
        env = os.getenv('APPDATA')

        if env == None:
            raise Exception('Windows section not containing Appdata? weird.')

        # FIXME: I know its bad, but right now i'll set it up statically to see how i can work on it later.
        return os.path.join(env, 'BetterDiscord', 'data', 'betterdiscord.asar')
