from abc import ABC, abstractmethod
import re


class AbstractPaths(ABC):
    @abstractmethod
    def get_discord_path(self):
        pass

    @abstractmethod
    def get_bc_path(self):
        pass

    def get_bc_asar_required_location(self, file: str) -> str | None:
        rx_get_better_discord_path = re.compile(r"^require\(\"(.*)\"\)\;$")

        with open(file, 'r') as f:
            for line in f:
                if ('betterdiscord.asar' in line) or ('BetterDiscord' in line):
                    val = re.match(rx_get_better_discord_path, line)

                    if val is None:
                        return None

                    val = val.group(1)
                    return val
