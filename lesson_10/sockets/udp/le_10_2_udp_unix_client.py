import socket
import pickle

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
unix_sock_name = 'unix.sock'
exit_app = ['q', 'quit', 'exit']
while True:
    try:
        message = input('You: ')
        if message in exit_app:
            raise Exception('Exit from app')
        message = pickle.dumps(message)

    except Exception:
        sock.close()
        break
    else:
        sock.sendto(message, unix_sock_name)