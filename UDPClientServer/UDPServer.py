import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this binds the process to this address and port
sock.bind(('127.0.0.1',12345))

while True:
    #recv module returns data and adress
    data,addr=sock.recvfrom(4096)  #inside it we write the number of bytes we want to accept
    print(str(data))
    #since the message should be in bytes and also encoded
    message=bytes("Hello I am UDP Server".encode('utf-8')) 
    sock.sendto(message,addr)