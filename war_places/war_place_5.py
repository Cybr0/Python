import socket
import pickle

app_clear = ('cls', 'clr', 'clear')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(5)
# sock.setblocking(False)
while True:
    try:
        print('Waiting...')
        client, addr = sock.accept()
        message = client.recv(1024)
        message = pickle.loads(message)
        client.close()
        if message.endswith(app_clear):
            name = message.split(':')
            print(f'Clear command from {name[0]}')
        else:
            print(message)
    except KeyboardInterrupt:
        sock.close()
        break
    except Exception:
        client.close()
