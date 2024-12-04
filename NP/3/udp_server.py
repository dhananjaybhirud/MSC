import socket
import threading

# Function to handle each client request
def handle_client(sock, addr):
    print(f"Connection from {addr}")
    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break
        print(f"Received from {addr}: {data.decode()}")
        sock.sendto(data, addr)  # Echo the data back to the client
    print(f"Connection closed from {addr}")

# Server setup
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("Server started and listening on port 12345...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        thread = threading.Thread(target=handle_client, args=(server_socket, client_address))
        thread.start()

if __name__ == "__main__":
    udp_server()