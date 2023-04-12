
import discord
import time
import asyncio
TOKEN = "" # discord bot token - type : str
CHANNEL_ID = 1 # channel token - type : int


class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)
        message = time.strftime('%Y.%m.%d - %H:%M:%S')
        await channel.send("eval end : "+message)   
        self.loop.create_task(self.shutdown())
    
    async def shutdown(self):
        await self.wait_until_ready()
        await asyncio.sleep(2)  # Change this value to the number of seconds before the bot shuts down
        await self.close()    

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)    
client.run(TOKEN)
