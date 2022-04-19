import requests

mp = input("Email:pass ").split(":")
token = requests.post("https://discord.com/api/v9/auth/login", json={"login": mp[0], "password": mp[1]})
print(token.text)