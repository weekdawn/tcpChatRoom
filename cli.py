import socket

s = socket.socket()
s.connect(('127.0.0.1',8080))

print 'Join the Chat Room...'
while True:
	s.send(raw_input('Me:'))
	data = s.recv(1024)
	if data == 'q':
		break
	else:
		print 'server:%s' % data
print 'You has quitted the Chat Room'
s.close()
