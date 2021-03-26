import modules.helper as h
import re
import os
import time

class command:
    def __init__(self):
        self.name = "installpro"
        self.description = "install substrate commands"

    def run(self, session, cmd_data):
        h.info_general("Uploading dylib 1/2...")
        if os.path.isfile("resources/espro.dylib"):
            session.upload_file("resources/espro.dylib", "/Library/MobileSubstrate/DynamicLibraries", ".espl.dylib")
            h.info_general("Uploading plist 2/2...")
            if os.path.isfile("resources/espro.plist"):
                session.upload_file("resources/espro.plist", "/Library/MobileSubstrate/DynamicLibraries", ".espl.plist")
                h.info_general("Respring...")
                time.sleep(1)
                session.send_command({"cmd": "killall", "args": "SpringBoard"})
            else:
                print("Unable to find espro.plist! (resources/espro.plist)")
        else:
            print("Unable to find espro.dylib! (resources/espro.dylib)")