import paramiko 
from paramiko.auth_handler import AuthenticationException, SSHException


class Command_client:
    def __init__(self):
        
        print("init")

    def _connect(self):
        #todo read from file or db 
        server = 'someip'
        port = 22
        user = 'someuser'
        pwd = 'somepassword'
        print("connect to ", server)
        try:
            self.sshClient = paramiko.SSHClient()
            self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.sshClient.connect(server, port, username=user, password=pwd) 
        except AuthenticationException  as error:
            # print(error)
            raise error
        return self.sshClient 

    def execute_command(self, cmd):
        self.conn = self._connect()
        stdin,stdout,stderr = self.sshClient.exec_command(cmd)
        # print (cmd)
        lines = stdout.readlines()
        msg = ''.join(lines) 
        # print(msg)
        return msg  

    def close(self):
        if self.conn:
            print("close")
            self.sshClient.close()

if __name__ == '__main__': 
    App = Command_client()
    #App.connect()
    msg = App.execute_command("date")
    print (msg) 
    App.close()
    
