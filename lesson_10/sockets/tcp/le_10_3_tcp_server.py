import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
# print(type(sock))
# print(sock)
while True:
    try:
        client, addr = sock.accept()
        # print(client)
        # print(addr)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print('Client: ', result.decode('utf-8'))
