import websocket, json, threading, time, random, requests
from utils import info
from storage.title import Logo
from leet.leets import leet_main
logo = Logo("e v e r e s t")

class WebsocketConn:
	def __init__(self, token, author):
		self.ws = websocket.WebSocket()
		self.interval = None
		self.token = token
		self.author = author

	def send(self, payload):
		self.ws.send(json.dumps(payload))

	def receive(self):
		response = self.ws.recv()
		if response:
			return json.loads(response)

	def heartbeat(self):
	    while True:
	        time.sleep(self.interval * random.randint(0, 1))
	        self.send({"op": 1, "d": "null"})

	def start_self(self):
		self.ws.connect("wss://gateway.discord.gg/")
		event = self.receive();print(info("Heartbeat Started"))
		self.interval = event["d"]["heartbeat_interval"] / 1000
		threading._start_new_thread(self.heartbeat, ())
		payload = {
		    "op": 2,
		    "d": {
		        "token": self.token,
		        "intents": 9216,
		        "properties": {"$os": "linux/windoself.ws", "$broself.wser": "firefox", "$device": "computer"},
		    },
		}

		self.send(payload)
		while True:
			event = self.receive()
			if event["t"] == "READY":
				print(info("Heartbeat Connected"))
			if event["t"] == "MESSAGE_REACTION_ADD" and event["d"]["user_id"] == self.author:
				channel_id = event["d"]["channel_id"]
				print(info(f"Sending to ({channel_id})"))
				print(logo.watermark("messenger"), end="")
				msg = input("> ")
				msg = leet_main(msg)
				requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", json={"content": msg}, headers={"Authorization": self.token})
