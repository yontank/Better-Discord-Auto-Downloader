from abc import ABC, abstractmethod
import os
import requests


class AbstractInstaller(ABC):

    @abstractmethod
    def install_bc(self, path: str) -> str | None:
        pass

    @abstractmethod
    def install_discord(self) -> str | None:
        pass

    def download_bc_asar_file(self, bc_path: str):
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
