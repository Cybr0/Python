import os
import socket
import pickle
unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind(unix_sock_name)
if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)
while True:
    try:
        print('Waiting new user message')
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = pickle.loads(result)
        print('Tim:', result)
