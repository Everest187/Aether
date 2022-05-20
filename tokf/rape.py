from tokf.sck import ScketConn

def raper(token):
	sck = ScketConn(token)
	sck.conn()
	sck.theme()