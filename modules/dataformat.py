import datetime, modules.helper

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
         
