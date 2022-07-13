import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    HOST, PORT = "localhost", 2048
    sock.connect((HOST, PORT))
    while True:
        data = input("Type the message to send:")
        data_bytes = data.encode()  # (str to bytes)
        sock.sendall(data_bytes)  # Send
        data_bytes = sock.recv(1024)  # Receive
        data = data_bytes.decode()  # (bytes to str)
        print("Received:", data)
