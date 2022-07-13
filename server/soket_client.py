import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    HOST, PORT = "localhost", 2048
    sock.connect((HOST, PORT))
    while True:
        data = input("Введите число: ")
        data_bytes = data.encode()
        sock.sendall(data_bytes)
        data_bytes = sock.recv(1024)
        data = data_bytes.decode()
        print("Ответ сервера:", data)
