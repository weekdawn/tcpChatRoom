import socket
import threading

def tcpLick(sock, addr):
	ip,port = addr
	print 'start a new connecting from %s:%s' % addr
	while True:
		data = sock.recv(1024)
		print "client%s:%s" % (port, data)
		if data == 'q':
			sock.send(data)
			break
		else:
			sock.send(data)
	sock.close()
	print 'closed a connection from %s:%s' % addr

s = socket.socket()
s.bind(('127.0.0.1',8080))
s.listen(5)

print "waiting for connecting..."
while True:
	conn, addr = s.accept()
	t = threading.Thread(target=tcpLick, args=(conn,addr))
	t.start()
conn.close()
print 'connecting is closed'


	
	