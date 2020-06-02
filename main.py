import client
import telegram_sender

from config import (
    host,
    port,
    user,
    pwd,
    path ,
    api_server,
    api_path
)


def main():
    print("Program Start")

    print (host,port,user,pwd)

    # ssh connection 
    App = client.CommandClient(host,port,user,pwd)
    msg = App.execute_command("date && uname -a")
    print (msg)
    App.close()

    # send telegram 
    Sender = telegram_sender.TelegramSender( api_server, api_path )
    response = Sender.send_message(msg)
    print (response)

if __name__ == '__main__': 
    main()