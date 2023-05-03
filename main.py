import discord
import os
import sys
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  channel = client.get_channel(int(os.getenv("CHANNEL_ID")))

  magnet_state = sys.argv[1];

  await channel.send(f"The club room is now {magnet_state}")

client.run(os.getenv("TOKEN"))