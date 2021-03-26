import datetime, helper

def print_formatted_convo(convo : dict):
    '''Prints a formatted and readable dumped sms/imessage conversation'''
    for message in convo['data']:
        selected_color = helper.RED if message["is_from_me"] == 1 else helper.CYAN
        sender = convo["partner"] if message["is_from_me"] == 1 else "Target"
        date = datetime.datetime.fromtimestamp((message["timestamp"] / 1000000000.0) + 978307200).strftime('%Y-%m-%d %H:%M:%S')
        print(("{color}[{date}] {person}: {text} " + helper.ENDC).format(
                color=selected_color,
                date=date,
                person=sender,
                text=(message["text"]).replace("\n", " ")
            ))
         