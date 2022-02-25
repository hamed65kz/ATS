# https://docs.telethon.dev/en/latest/examples/chats-and-channels.html
# https://github.com/LonamiWebs/Telethon
import time

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from datetime import datetime, timedelta
import asyncio

class TelegramClientClass:
    __name = None
    __api_id = None
    __api_hash = None
    __client: TelegramClient = None
    __lastDollarUpdateTime = None
    __dollarPrice_Toman = 0

    @staticmethod
    def connect():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            TelegramClientClass.__name = "atsapp"
            TelegramClientClass.__api_id = 13200132
            TelegramClientClass.__api_hash = '9d68b97f30af0fcf3f469fac45a69710'
            TelegramClientClass.__client = TelegramClient('HamedTelegramAccount', TelegramClientClass.__api_id,
                                                          TelegramClientClass.__api_hash)
            TelegramClientClass.__client.start()
            TelegramClientClass.getLastPrice()

            # with TelegramClientClass.__client:
            #     TelegramClientClass.__client.loop.run_until_complete(TelegramClientClass.getLastDollarPriceInRial())

        except Exception as ex:
            TelegramClientClass.__client = None
            print('can not connect to telegram : ' + str(ex))


    @staticmethod
    def getLastPrice():
        now = int(datetime.now().timestamp())
        lasttime=TelegramClientClass.__lastDollarUpdateTime if TelegramClientClass.__lastDollarUpdateTime is not None else 0
        diff= now - lasttime
        if diff>10 or TelegramClientClass.__lastDollarUpdateTime is None:
            if TelegramClientClass.__client is None:
                TelegramClientClass.connect()
            try:
                iterm = TelegramClientClass.__client.iter_messages('arzdolar')
                message = next(iterm)
                tmp=message.text[18:24]
                tmp=tmp.replace(',', '')
                TelegramClientClass.__dollarPrice_Toman=int(tmp)
                TelegramClientClass.__lastDollarUpdateTime=now
                print("dollar price is " + str(TelegramClientClass.__dollarPrice_Toman) + " Toman :  " + str(int(time.time())))
            except Exception as ex:
                print('can not get data from telegram : ' + str(ex))
            return TelegramClientClass.__dollarPrice_Toman
        else:
            return TelegramClientClass.__dollarPrice_Toman
