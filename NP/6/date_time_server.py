import socket
import datetime

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 12345)
sock.bind(server_address)

print("Server is listening on {}:{}".format(*server_address))

while True:
    # Wait for a client to send a request
    data, address = sock.recvfrom(4096)
    print("Received request from:", address)

    # Get the current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Send the date and time back to the client
    sock.sendto(current_time.encode(), address)