import socket
import sys
import select

name = input("Player name: ")
HOST = input("Join a server: ")
PORT = input("Join a room: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((HOST, PORT))
except:
	print("Room doesn't exist, shutting down")
	sys.exit()

print("Joined game")

socketList = [sys.stdin, s]

while True:
	r, w, e = select.select(socketList, [], [])

	for sock in r:
		if sock == s:
			data = sock.recv(1024)
			if not data:
				print("Disconnected")
				sys.exit()

			else:
				print(data.decode())
				sys.stdout.write('\r[Me] '); sys.stdout.flush()
		else:
			msg = sys.stdin.readline()
			s.send(msg.encode())
			sys.stdout.write("\r[Me] "); sys.stdout.flush()