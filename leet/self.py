import websocket, json, threading, time, random, requests
from utils import info, close
from storage.title import Logo
from leet.leets import leet_main
from storage.exceptions import CustomError
from cfg_r import ocfg

from colorama import Fore

logo = Logo("e v e r e s t")


class WebsocketConn:
    def __init__(self, token, author):
        self.channelid = []
        self.prefix = ocfg("cfg.json")["Discord"]["prefix"]
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

    def leet_send(self):
        while True:
            for channel_id in filter(lambda c: len(c) != 0, self.channelid):
                info(f"Sending to ({channel_id})")
                msg = Logo("").watermark("messenger")
                msg = leet_main(msg)
                requests.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages",
                    json={"content": msg},
                    headers={"Authorization": self.token},
                )

    def leet_conn(self):
        try:
            self.ws.connect("wss://gateway.discord.gg/")
            event = self.receive()

            info("Heartbeat Started")
            self.interval = event["d"]["heartbeat_interval"] / 1000
            heartbeat_thr = threading.Thread(target=self.heartbeat)
            heartbeat_thr.start()
            payload = {
                "op": 2,
                "d": {
                    "token": self.token,
                    "intents": 4608,
                    "properties": {
                        "$os": "linux/windows",
                        "$browser": "firefox",
                        "$device": "computer",
                    },
                },
            }

            self.send(payload)
            send_thr = threading.Thread(target=self.leet_send)
            send_thr.start()
            while True:
                event = self.receive()
                command = ocfg("cfg.json")["Discord"]["Leet"]["selected_channel"]
                if event["t"] == "READY":
                    info("Logged in to Discord")

                elif (
                    event["t"] == "MESSAGE_CREATE"
                    and event["d"]["author"]["id"] == self.author
                    and event["d"]["content"].startswith(f"{self.prefix}{command}")
                ):
                    channel_id = event["d"]["channel_id"]
                    self.channelid.clear()
                    self.channelid.append(channel_id)

        except KeyboardInterrupt:
            info(
                f"\n{Fore.YELLOW}requested shutdown, going back to main...{Fore.RESET}\r"
            )
            raise CustomError("Back To Main")

    def auto_response(self):
        channelid = []
        try:
            self.ws.connect("wss://gateway.discord.gg/")
            event = self.receive()
            info("Heartbeat Started")
            self.interval = event["d"]["heartbeat_interval"] / 1000
            threading._start_new_thread(self.heartbeat, ())
            payload = {
                "op": 2,
                "d": {
                    "token": self.token,
                    "intents": 16384,
                    "properties": {
                        "$os": "linux/windoself.ws",
                        "$broself.wser": "firefox",
                        "$device": "computer",
                    },
                },
            }

            self.send(payload)
            while True:
                event = self.receive()
                if event["t"] == "READY":
                    info("Logged in to Discord")

                elif event["t"] == "TYPING_START":
                    channel_id = event["d"]["channel_id"]
                    channelid.append(channel_id)
                    channelid.clear() if len(channelid) >= 2 else None
                    try:
                        if channelid[0] == channel_id and len(channelid) == 1:
                            info(f"Sending to ({channel_id})")
                            message = ocfg("cfg.json")
                            msg = message["Discord"]["AutoRes"]["message"]
                            requests.post(
                                f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                json={"content": msg},
                                headers={"Authorization": self.token},
                            )
                    except IndexError:
                        pass
        except KeyboardInterrupt:
            info(
                f"\n{Fore.YELLOW}requested shutdown, going back to main...{Fore.RESET}\r"
            )
            raise CustomError("Back To Main")
