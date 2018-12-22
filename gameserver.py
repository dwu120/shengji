import socket
import select
import sys
import threading
import queue

HOST = '127.0.0.1'
PORT = 8081
# socket : player object
playersList = {}
numPlayers = 4
numDecks = 2

toSend = queue.Queue()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

def listen():
	while True:
		r, w, e = select.select(socketList, [], [])

		for sock in r:
			if sock == s:
				newSock, addr = s.accept()
				socketList.append(newSock)
				msg = "Client " + str(addr) + " has connected"
				print(msg)
				toSend.put((msg.encode(), None))

			else:
				data = sock.recv(4096)
				if data:
					msg = str(sock.getpeername()) + ": " + data.decode()
					print(msg.rstrip())
					toSend.put((msg.encode(), sock))
				else:
					msg = "Client " + str(sock.getpeername()) + " has disconnected"
					print(msg)
					toSend.put((msg.encode(), sock))
					socketList.remove(sock)

def broadcast(msgtuple):
	for sock in socketList:
		if sock != msgtuple[1] and sock != s:
			sock.send(msgtuple[0])

s.listen(10)
socketList.update({s : })
print("Server started on " + HOST, str(PORT))

recv_thread = threading.Thread(target=listen)
recv_thread.start()

while True:
	broadcast(toSend.get())




def game_setup():
