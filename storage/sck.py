import socket, ssl
from random import randint

class ScketConn:
	def __init__(self):
		self.sock = None
		self.byte = 2064

	def conn(self):
		socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socks.connect(("discord.com", 443))
		wrap = ssl.create_default_context().wrap_socket(socks, server_hostname="discord.com")
		self.sock = wrap
