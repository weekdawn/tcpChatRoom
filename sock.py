import socket
import threading

def newSock(sock, addr):
	ip,port = addr
	print 'start a new connecting from %s:%s' % addr
	while True:
		sock.setblocking(True)
		data = sock.recv(1024)
		print "client%s:%s" % (port, data)
		if data == 'q':
			sock.send(data)
			break
		else:
			sock.send(data)
	sock.close()
	print 'closed a connection from %s:%s' % addr

class TcpCreate:
	def __init__(self):
		self.s = socket.socket()

	def startConnect(self):
		print "start a tcp server"
		print "a tcp server has launched"
		self.s.bind(('127.0.0.1',8080))
		self.s.listen(5)
		print "waiting for connecting..."
		while True:
			conn, addr = self.s.accept()
			t = threading.Thread(target=newSock, args=(conn,addr))
			t.start()
		conn.close()
		print 'connecting is closed!'

if __name__ == "__main__":
	p = TcpCreate()
	p.startConnect()
	
	