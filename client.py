import paramiko 
from paramiko.auth_handler import AuthenticationException, SSHException

class CommandClient:
    def __init__(self, host,port,user,pwd):
        print("init")
        self.host = host 
        self.port = port 
        self.user = user 
        self.pwd = pwd 
    
    def _connect(self):
        #todo read from file or db 

        try:
            self.sshClient = paramiko.SSHClient()
            self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            self.sshClient.connect(self.host, self.port, username=self.user, password=self.pwd) 
        except AuthenticationException  as error:
            # print(error)
            raise error
        return self.sshClient 

    def execute_command(self, cmd):
        self.conn = self._connect()
        stdin,stdout,stderr = self.sshClient.exec_command(cmd)
        lines = stdout.readlines()
        msg = ''.join(lines) 
        return msg  

    def close(self):
        if self.conn:
            self.sshClient.close()

if __name__ == '__main__': 
    App = CommandClient(host, port, user, pwd )
    #App.connect()
    msg = App.execute_command("date")
    #print (msg) 
    App.close()
    
