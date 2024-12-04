import socket

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 5000

def start_server():
    # Create a socket object with IPv4 addressing and TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    
    # Listen for incoming connections (max 1 client in the queue)
    server_socket.listen(1)
    print(f"Server started. Listening for connections on {SERVER_HOST}:{SERVER_PORT}...")
    
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address[0]}:{client_address[1]}")
        
        while True:
            try:
                # Receive message from the client (up to 1024 bytes)
                message = client_socket.recv(1024).decode('utf-8')
                
                if not message:
                    # If no message is received, the client has disconnected
                    break
                
                print(f"Received from {client_address[0]}:{client_address[1]}: {message}")
                
                # Echo the message back to the client
                client_socket.send(message.encode('utf-8'))
                
            except ConnectionResetError:
                print(f"Client {client_address[0]}:{client_address[1]} disconnected.")
                break
        
        # Close the client socket
        client_socket.close()

if __name__ == '__main__':
    start_server()