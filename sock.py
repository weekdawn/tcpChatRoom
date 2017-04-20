import socket

s = socket.socket()
s.bind(('127.0.0.1',8080))
s.listen(5)

conn, addr = s.accept()
print "connecting..."
while True:
	data = conn.recv(1024)
	print 'client:%s' % data
	if data == 'q':
		conn.send(data)
		break
	conn.send(data)
conn.close()
print 'connecting is closed'


	
	