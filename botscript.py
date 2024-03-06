# This example requires the 'message_content' intent.

import discord
import requests

WEBHOOK_URL = "YOUR WEBHOOK URL"
processed_messages = set()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # check if user receives a DM
        if isinstance(message.channel, discord.channel.DMChannel):
            if message.id not in processed_messages:
                processed_messages.add(message.id)
                data = {
                    'content': f"New DM from {message.author}: {message.content}"
                }
                requests.post(WEBHOOK_URL, json=data)

                print(f"Received DM from {message.author}: {message.content}")

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages= True

client = MyClient(intents=intents)
client.run('YOUR TOKEN')
