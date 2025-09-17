from venv import create
from installer import *
from paths import *


def main():
    discord_path = get_discord_path()
    appdata_path = os.getenv("APPDATA")
    if appdata_path == None:
        raise Exception("Not Running In Windows")

    if not discord_path:
        raise Exception("Didn't Find discord path.")

    if not (os.path.join(os.getenv('APPDATA', 'BetterDiscord'))):
        if create_bc_path() == None:
            raise Exception("Couldn't Install Better Discord ")

    # Get ASAR File location from discord, if set.
    bc_asar_path = get_bc_asar_location(discord_path)

    if bc_asar_path == None:
        # Inject the file with Better Discords code, by requiring it to run.
        with open(discord_path, 'w') as injection_file:
            injection_file.write(
                f'\nrequire({os.path.join(appdata_path, "BetterDiscord", "data", "betterdiscord.asar")});')

    return


if __name__ == '__main__':
    main()
