import requests
import time
import random, string
from discord import Webhook, RequestsWebhookAdapter
from discord_webhook import DiscordEmbed, DiscordWebhook

print("███████╗██╗  ██╗██╗   ██╗██╗     ██╗     ██╗  ██╗")
print("██╔════╝██║ ██╔╝██║   ██║██║     ██║     ╚██╗██╔╝")
print("███████╗█████╔╝ ██║   ██║██║     ██║      ╚███╔╝ ")
print("╚════██║██╔═██╗ ██║   ██║██║     ██║      ██╔██╗ ")
print("███████║██║  ██╗╚██████╔╝███████╗███████╗██╔╝ ██╗")
print("╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝")
print("")
print("Join our discord server for support!")
print("Discord: https://discord.gg/37bd2sHJ")

link = input("Please enter the link of the webhook: ")
amount = int(input("How many codes do you want to generate?: "))
for i in range(amount):
    time.sleep(5)
    code = "https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=16))
    print("[Generated] " + code)
    webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
    webhook.send(code)
    