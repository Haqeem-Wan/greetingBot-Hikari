import hikari
from dotenv import load_dotenv
import os

load_dotenv("..\Bot_Env\greetingBot-hikari.env")
TOKEN = os.getenv('DISCORD_TOKEN')
check = str(TOKEN)
bot = hikari.GatewayBot(token=str(TOKEN))
bot.run()