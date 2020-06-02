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

from cmd import commands


def main():
    print("Program Start")

    print (host,port,user,pwd)
    
    App = client.CommandClient(host,port,user,pwd)
    
    results = []
    
    for values in commands : 
        # print (values['host'],values['cmd_name'], values['cmd'], values['expect'])

        _host = values['host']
        _cmd = values['cmd']
        _alias = values['alias']

        if _host == host:
            result = _alias + ":" + values['cmd_name'] + ":" 
            msg = App.execute_command( _cmd )
            if int(msg) == values['expect']:
                result = result + "정상"
            else:
                result = result + "비정상"
            
            results.append(result)
            App.close()

    Sender = telegram_sender.TelegramSender( api_server, api_path )
    
    msg =""
    for value in results:
        msg = msg + value + "\n"
    response = Sender.send_message(msg)
    print (response)

if __name__ == '__main__': 
    main()