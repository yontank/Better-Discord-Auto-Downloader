from typing import override
from abstract import abstract_installer
import psutil
import os
from turtle import down
import requests


from paths.windows_paths import WindowsPaths


class WindowsInstaller(abstract_installer.AbstractInstaller):

    def install_bc(self, path: str):
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

        if not super().download_bc_asar_file(os.path.join(path, 'data', 'betterdiscord.asar')):
            return None

        return os.path.join(path, 'data', 'betterdiscord.asar')

    def install_discord(self) -> str | None:
        raise NotImplementedError()

    def execute(self):
        paths = WindowsPaths()
        proc_name = 'discord.exe'

        discord_inject_file = paths.get_discord_path()

        if (discord_inject_file == None):
            raise Exception('Cannot find discord path')

        for proc in psutil.process_iter():
            if proc.name().lower() == proc_name:
                proc.kill()
        # Todo: Write into Injection file, adding the asar file from Better Discord.
        try:
            with open(discord_inject_file, 'w') as OF:
                OF.writelines(
                    ["module.exports = require('./core.asar');\n", f"require('{paths.get_bc_path().replace('\\', '\\\\')}');"])
        except Exception as e:
            print(e)
