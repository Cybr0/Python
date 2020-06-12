import socket
import pickle
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print(socket.AF_INET)
# print(socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 8888))
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
