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

    # print (host,port,user,pwd)
    
    App = client.CommandClient(host,port,user,pwd)
    
    results = []

    _alias= "" 
    for values in commands : 
        # print (values['host'],values['cmd_name'], values['cmd'], values['expect'])

        _host = values['host']
        _cmd = values['cmd']
        _alias = values['alias']

        # results.append("[" + _alias + "]")

        print (results)

        if _host == host:
            result =  values['cmd_name'] + ":" 
            resp_msg = App.execute_command( _cmd )
            if int(resp_msg) == values['expect']:
                result = result + "정상"
            else:
                result = result + "비정상"
            
            results.append(result)
            App.close()

    Sender = telegram_sender.TelegramSender( api_server, api_path )
    
    msg = "[" + _alias + "] \n"
    for value in results:
        msg = msg + value + "\n"
    response = Sender.send_message(msg)
    print (response)

if __name__ == '__main__': 
    main()