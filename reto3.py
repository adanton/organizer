from pathlib import Path
from gi.repository import GLib
import tomli

def main():

    with open("~/.config/diogenes/diogenes.conf", "rb") as f:
        toml_dict = tomli.load(f)

    try:
        toml_dict = tomli.loads("]] this is invalid TOML [[")
    except tomli.TOMLDecodeError:
        print("Yep, definitely not valid.")


    try:
        downloads_dir = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
        print(f"\nDirectory: {downloads_dir}\n")
        if downloads_dir.is_dir():
            for one_file in downloads_dir.iterdir():
                if not one_file.is_dir():
                    print(one_file.name)
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()