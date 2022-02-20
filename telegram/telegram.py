#https://docs.telethon.dev/en/latest/examples/chats-and-channels.html
#https://github.com/LonamiWebs/Telethon
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from datetime import datetime, timedelta

name="atsapp"
api_id = 13200132
api_hash = '9d68b97f30af0fcf3f469fac45a69710'
client = TelegramClient('HamedTelegramAccount', api_id, api_hash)
client.start()
iterm=client.iter_messages('arzdolar')
message=next(iterm)
print(message.date+timedelta(hours=3,minutes=30), ',', str(message.text))
# for message in client.iter_messages('arzdolar'):
#     print(message.date, ':', message.text)
#     break