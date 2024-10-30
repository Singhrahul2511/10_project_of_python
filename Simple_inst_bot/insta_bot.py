
# from instabot import Bot
# bot =Bot()
# bot.login(username = "Singhrahul2.0",password = "Rahul#2511")
# bot.follow('viralfans25')
import os
from instabot import Bot

username = os.getenv("Singhrahul2.0")
password = os.getenv("Rahul#2511")

bot = Bot()
bot.login(username= 'Singhrahul2.0', password='Rahul#2511')
bot.follow('viralfans25')
