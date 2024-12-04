import socket
import threading
HOST = 'localhost'  
PORT = 5000         
clients = []
def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
               break
            print(f"Received from {client_address[0]}:{client_address[1]}: {message}")
            broadcast(message, client_socket)
        except ConnectionResetError:
            print(f"Client {client_address[0]}:{client_address[1]} disconnected.")
            break
    client_socket.close()
    clients.remove(client_socket)
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except BrokenPipeError:
                client.close()
                clients.remove(client)
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server started. Listening for connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address[0]}:{client_address[1]}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
if __name__ == '__main__':
    start_server()