import datetime, modules.helper, os

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
         
def print_formatted_history(history : dict):
    '''Prints a formatted and readable dumped safari history'''
    rows, cols = os.popen('stty size', 'r').read().split()
    for history_item in history:
        formatted_p = str("{:^12.10s}| {:<" + str((int(cols) - 12) - 2) + "." + str((int(cols) - 12) - 2) + "s}")
        print(formatted_p.format(
            history_item["date"],
            history_item["details"]["url"],
            "eee"
        ))
