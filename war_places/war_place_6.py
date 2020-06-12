import socket
import pickle
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_name = 'Tim: '
app_exit = ['q', 'quit', 'exit']
app_clear = ['cls', 'clr', 'clear']
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 8888))
        message = input('You: ')
        if message in app_exit:
            raise Exception('Command: exit  from app')
        elif message in app_clear:
            os.system('cls')
        user_message = pickle.dumps(user_name + message)
        sock.send(user_message)
    except socket.error:
        sock.close()
    except Exception:
        sock.close()
        break
