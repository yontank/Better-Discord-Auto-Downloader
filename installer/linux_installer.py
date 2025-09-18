from abstract.abstract_installer import AbstractInstaller
import os
from turtle import down
import requests


class LinuxInstaller(AbstractInstaller):
    def install_bc(self, path: str) -> str | None:
        raise NotImplementedError()

    def install_discord(self) -> str | None:
        raise NotImplementedError()
