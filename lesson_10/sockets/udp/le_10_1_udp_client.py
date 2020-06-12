import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
        sock.sendto(message, ('127.0.0.1', 8888))
