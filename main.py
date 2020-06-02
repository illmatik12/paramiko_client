import client
import telegram_sender

def main():
    print("Program Start")

    # ssh connection 
    App = client.Command_client()
    msg = App.execute_command("date && uname -a")
    print (msg)
    App.close()

    #send telegram 
    Sender = telegram_sender.Telegram_Sender()
    response = Sender.send_message(msg)
    print (response)


if __name__ == '__main__': 
    main()