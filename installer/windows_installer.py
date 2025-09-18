from typing import override
from abstract import abstract_installer

import os
from turtle import down
import requests


class Windows(abstract_installer.AbstractInstaller):

    @override
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
