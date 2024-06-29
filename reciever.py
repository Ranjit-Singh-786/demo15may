import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # MEDIUM , PROTOCOL
# ip address  
ip_address = "192.168.1.25"
# ip_address = "127.0.0.1"
port_no = 2525  
my_address = (ip_address,port_no)
s.bind(my_address)

while True:
    data = s.recvfrom(100)
    message = data[0]
    sender_address = data[1]  # (ip,port)
    sender_ip = sender_address[0]
    message = message.decode("ascii")

    with open(str(sender_ip)+".txt",'a+') as file: 
        file.write(message+"\n")
    print(message)

    # ip address , message 
    # file handling 
    # ipadress.txt -->  










# ip_address = "127.0.0.1"    # localhost
