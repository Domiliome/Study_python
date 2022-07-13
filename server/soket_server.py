import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(("localhost", 2048))
server_sock.listen(5)
while True:
    sock, addr = server_sock.accept()
    while True:
        data = sock.recv(1024)  # Receive
        result = int(data.decode()) * 10 # (bytes to str)
        data = str(result).encode()
        sock.sendall(data)  # Send