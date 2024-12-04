import socket 

port = 60000 
s = socket.socket()
host = socket.gethostname() 
s.bind((host, port)) 
s.listen(5) 
print('\nServer listening....') 
while True:
    conn, addr = s.accept() 
    print('\nGot connection from', addr)    
    data = conn.recv(1024)
    print('\nServer received', repr(data)) 
    
    filename = 'npfile.txt' 
    f = open(filename, 'rb') 
    l = f.read(1024) 
    
    while l: 
        conn.send(l) 
        print('\nSent', repr(l)) 
        l = f.read(1024) 
    
    f.close() 

    print('\nDone sending') 
    conn.send(str.encode('\nThank you for connecting'))
    conn.close() 