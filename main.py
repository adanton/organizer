from pathlib import Path
from gi.repository import GLib


def main():
    try:
        downloads_dir = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
        print(f"\nDirectory: {downloads_dir}\n")
        if downloads_dir.is_dir():
            for one_file in [
                    x for x in downloads_dir.iterdir() if not x.is_dir()]:
                print(one_file.name)
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    main()