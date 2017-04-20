import socket

s = socket.socket()
s.connect(('127.0.0.1',8080))

print 'connecting the server...'
while True:
	s.send(raw_input('client:'))
	data = s.recv(1024)
	if data == 'q':
		break
	else:
		print 'server:%s' % data
print 'connecting has closed'
s.close()
