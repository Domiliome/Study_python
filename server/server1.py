import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("localhost", 2048))
server_sock.listen(1)   # количество клиентов
while True:
    sock, addr = server_sock.accept()
    while True:
        data = sock.recv(1024)
        result = data.decode()
        result = int(result) * 10
        data = str(result).encode()
        sock.sendall(data)
