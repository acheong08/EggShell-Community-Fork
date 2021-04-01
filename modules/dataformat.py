import datetime, modules.helper, os

def print_formatted_whatsapp(chat_storage : dict):
    '''Prints a formatted and readable dumped whatsapp conversation'''
    for message in chat_storage['data']:
        selected_color = modules.helper.RED if message["is_from_me"] == 1 else modules.helper.CYAN
        sender = chat_storage["partner"] if message["is_from_me"] == False else "Target"
        date = datetime.datetime.fromtimestamp((message["timestamp"]) + 978307200).strftime('%Y-%m-%d %H:%M:%S')
        print(("{color}[{date}] {person}: {text} " + modules.helper.ENDC).format(
                color=selected_color,
                date=date,
                person=sender,
                text=(message["text"]).replace("\n\n", "\n").replace("\n", ("\n" + (" " * (len(date) + 3))))
            ))
         
def print_formatted_convo(convo : dict):
    '''Prints a formatted and readable dumped sms/imessage conversation'''
    for message in convo['data']:
        selected_color = modules.helper.RED if message["is_from_me"] == 1 else modules.helper.CYAN
        sender = convo["partner"] if message["is_from_me"] == 1 else "Target"
        date = datetime.datetime.fromtimestamp((message["timestamp"] / 1000000000.0) + 978307200).strftime('%Y-%m-%d %H:%M:%S')
        print(("{color}[{date}] {person}: {text} " + modules.helper.ENDC).format(
                color=selected_color,
                date=date,
                person=sender,
                text=(message["text"]).replace("\n", " ")
            ))
         
def print_formatted_bookmarks(bookmarks : dict):
    '''Prints a formatted and readable dumped safari bookmark list'''
    # TODO: Fix this function to actually format everythings
    for bookmark in bookmarks:
        print(str(bookmark))

def print_formatted_history(history : dict):
    '''Prints a formatted and readable dumped safari webhistory'''
    rows, cols = os.popen('stty size', 'r').read().split()
    for history_item in history:
        formatted_p = str("{:^12.10s}| {:<" + str((int(cols) - 12) - 2) + "." + str((int(cols) - 12) - 2) + "s}")
        print(formatted_p.format(
            history_item["date"],
            history_item["details"]["url"],
            "eee"
        ))

def print_formatted_voicemails(voicemail : dict):
    '''Prints a formatted and readable dumped voicemail database'''
    for vm in voicemail["data"]:
        print("{color_start}[{time}]{color_normal} {sender} ---> {receiver} ({duration}s)".format(
                color_start=modules.helper.COLOR_INFO,
                color_normal=modules.helper.WHITE,
                time=datetime.datetime.fromtimestamp(int(vm["timestamp"]) + 978307200).strftime('%Y-%m-%d %H:%M:%S'),
                sender=vm["sender"],
                receiver=vm["receiver"],
                duration=vm["duration"]
            ))