import socket, ssl

class ScketConn:
	def __init__(self, token):
		self.sock = None
		self.byte = 2064
		self.token = token

	def conn(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(("discord.com", 443))
		self.sock = ssl.create_default_context().wrap_socket(self.sock, server_hostname='discord.com')

	def theme(self):
		self.sock.send(f"PATCH /api/v9/users/@me/settings HTTP/1.1\r\nHost: discord.com\r\nContent-Type: application/json\r\nAuthorization: {self.token}\r\ntheme: light\r\n\r\n".encode())
		print(self.sock.recv(self.byte).decode("utf-8"))
		self.sock.close()