import socket

HOST, PORT = "localhost", 2048
connections = []
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)
        serv_sock.setblocking(False)  # Important!
        while True:
            try:
                #print("Try to accept a new connection...")
                sock, addr = serv_sock.accept()
                sock.setblocking(False)
                print("Connected by", addr)
                connections.append((sock, addr))
            except BlockingIOError:
                print("No connections are waiting to be accepted")
                pass
            for sock, addr in connections.copy():
                #print("Try to receive data from:", sock, addr)
                try:
                    data = sock.recv(1024)
                except ConnectionError:
                    print(f"Client suddenly closed while receiving from {addr}")
                    connections.remove((sock, addr))
                    sock.close()
                    continue
                except BlockingIOError:
                    # No data received
                    continue
                print(f"Received: {data} from: {addr}")
                if not data:
                    connections.remove((sock, addr))
                    sock.close()
                    print("Disconnected by", addr)
                    continue
                data = data.upper()
                print(f"Send: {data} to: {addr}")
                try:
                    sock.sendall(data)
                except ConnectionError:
                    print(f"Client suddenly closed, cannot send to {addr}")
                    connections.remove((sock, addr))
                    sock.close()
                    continue