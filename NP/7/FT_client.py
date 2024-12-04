import socket 

s = socket.socket() 
host = socket.gethostname()
port = 60000 
s.connect((host, port)) 
s.send(str.encode("\nHello server!")) 
with open('received_file', 'wb') as f:
    print('\nfile opened') 
    
    while True:
        print('receiving data...') 
        data = s.recv(1024) 
        print('data=%s', (data)) 
        
        if not data: 
            break
        
        f.write(data) 
    
    f.close() 

print('\nSuccessfully received the file')
s.close() 
print('\nconnection closed') 



