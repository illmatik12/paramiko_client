
# Telegram msg sender
## How to
* using paramiko 
* custom api 


## .env file 
```python
REMOTE_HOST=some host
REMOTE_PORT=port 
REMOTE_USER=some user 
REMOTE_PASSWORD=some user 

TELEGRAM_SERVER=http://customurl:5000
TELEGRAM_PATH=/1
```

## command file 
# cmd.py
```
commands = [
    { 'host':'127.0.0.1','alias':'test', 'cmd_name':'free','cmd':'echo 1', 'expect' : 1 },
    { 'host':'127.0.0.1','alias':'bpobackuptest', 'cmd_name':'disk_usage','cmd':'echo 2', 'expect' : 1 }
]

```