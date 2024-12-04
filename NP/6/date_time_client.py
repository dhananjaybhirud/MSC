import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 12345)

try:
    # Send a request for the date and time
    message = b'GET_DATE_TIME'
    sock.sendto(message, server_address)

    # Receive the response
    data, _ = sock.recvfrom(4096)
    print("Current Date and Time:", data.decode())

finally:
    sock.close()