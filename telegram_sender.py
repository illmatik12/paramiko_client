import requests



class TelegramSender:
    def __init__(self, host, api_path ):
        self.host = host 
        self.api_path = api_path #send api 
    
    def send_message(self, send_msg):
        url= self.host + self.api_path
        params  = {'send_msg' : send_msg}
        try:
            response = requests.get(url, params  = params)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return response

if __name__ == '__main__': 
    App = TelegramSender()
    response = App.send_message('test')
    print (response)
