import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    try:
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.sendto(message.encode(), server_address)

            # Receiving echo from the server
            data, server = client_socket.recvfrom(1024)
            print(f"Echo from server: {data.decode()}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    udp_client()