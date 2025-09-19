from email.policy import default
from pathlib import WindowsPath
from venv import create
from abstract.abstract_installer import AbstractInstaller
from installer import *
from installer.windows_installer import WindowsInstaller
from paths import *
import platform


def main():
    os_type = platform.system()
    print(os_type)

    installer = get_installer(os_type)
    if installer == None:
        return

    installer.execute()


def get_installer(os_type: str):
    match os_type:
        case "Windows":
            return WindowsInstaller()
        case "Linux":
            pass
        case _:
            raise Exception("Operating System not known")


def get_paths(os_type: str):
    match os_type:
        case "Windows":
            return WindowsPath()
        case "Linux":
            raise NotImplementedError()

    raise Exception("Operating System not known")


if __name__ == '__main__':
    main()
