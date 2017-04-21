import socket

server_ip, server_port = '127.0.0.1', 8080
s = socket.socket()
s.connect((server_ip,server_port))
client_ip, client_port = s.getsockname()

print "Join the Chat Room --%s : %s" % (server_ip,server_port)
print "Your chatID is %s" % client_port
while True:
	s.send(raw_input('Me : '))
	data = s.recv(1024)
	if data == 'quit':
		break
	print data
print 'You has quitted the Chat Room'
s.close()
