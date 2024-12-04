import socket

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 5000

def start_client():
    # Create a socket object with IPv4 addressing and TCP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server using the specified host and port
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to the server.")
    
    while True:
        # Read user input from the command line
        message = input("Enter message to send (or 'exit' to quit): ")
        
        if message.lower() == 'exit':
            print("Exiting...")
            break
        
        # Send the message to the server
        client_socket.send(message.encode('utf-8'))
        
        # Receive the echoed message from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")
    
    # Close the client socket
    client_socket.close()

if __name__ == '__main__':
    start_client()