#coding=utf-8
import socket
import threading

class TcpCreate:
	def __init__(self):
		self.s = socket.socket()

	def newSock(self,sock, addr):
		ip,port = addr
		while True:
			sock.setblocking(True)
			data = sock.recv(1024)
			print "%s : %s" % (port, data)
			if data == 'q':
				sock.send(data)
				break
			else:
				sock.send(data)
		sock.close()
		print '%s : %s has quitted the Chat Room' % addr
	
	def startConnect(self):
		self.s.bind(('127.0.0.1',8080))
		self.s.listen(5)
		print "creating chat room..."
		ipaddr,port = self.s.getsockname()
		print	"----------------Chat Room-------------------\n"\
				"---------address : %s\n"\
				"---------port    : %s\n"\
				"--------------------------------------------" % (ipaddr,port)
		while True:
			conn, addr = self.s.accept()
			ip,port = addr
			print "%s : %s has joined in the Chat room" % (ip,port)
			t = threading.Thread(target=self.newSock, args=(conn,addr))
			t.start()
		conn.close()
		print 'connecting is closed!'

if __name__ == "__main__":
	p = TcpCreate()
	p.startConnect()
	
	