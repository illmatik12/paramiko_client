import requests



class Telegram_Sender:
    def __init__(self):
        self.host = 'url'
        self.path = '/1' #send api 
    
    def send_message(self, send_msg):
        url= self.host + self.path
        params  = {'send_msg' : send_msg}
        try:
            response = requests.get(url, params  = params)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

if __name__ == '__main__': 
    App = Telegram_Sender()
    response = App.send_message('test')
    print (response)
