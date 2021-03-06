#coding=utf-8
import socket
import threading

class TcpCreate:
	def __init__(self):
		self.s = socket.socket()
		self.clientIDs = []

	def newSock(self,sock, addr):
		client_ip, client_port = addr
		while True:
			sock.setblocking(True)
			data = sock.recv(1024)
			saveRecord = "%s : %s" % (client_port, data)
			self.clientIDs.append(saveRecord)
			print saveRecord
			if data == 'q':
				sock.send('quit')
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
				"---------input 'q' to exit the Chat Room\n"\
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
	
	