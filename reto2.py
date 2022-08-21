import mimetypes
import re
from gi.repository import GLib
from pathlib import Path

mimetypes.init()

def main():
    try:
        downloads_dir = Path(GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD))
        print(f"\nDirectorio: {downloads_dir}\n")
        patron = r".*[0-9].*"
        if downloads_dir.is_dir():
            for index, afile in enumerate(downloads_dir.iterdir()):
            #for index, afile in enumerate downloads_dir.iterdir():
            #for index, afile in enumerate([x for x in downloads_dir.iterdir() if not x.is_dir()]):
                if afile.is_file():
                    if re.match(patron, afile.name):
                        nombre = afile.name.lower()
                    else:
                        nombre = afile.name.upper()
                    #nombre = afile.name.lower() if re.match(patron, afile.name) else afile.name.upper()
                    if mimetypes.guess_type(afile)[0] == "image/jpeg":
                        if index % 2 == 0:
                            print(index, f" => \"{nombre}\"")
                        else:
                            print(index, nombre)
    except Exception as exception:
        print(exception)

if __name__ == "__main__":
    main()
