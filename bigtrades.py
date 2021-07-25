import twitter



api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')


def tweet(text):
    status = api.PostUpdate(text)


import os
import sys
sys.path.append('../../../')

from bfxapi import Client

bfx = Client(
)

@bfx.ws.on('error')
def log_error(err):
  print ("Error: {}".format(err))


@bfx.ws.on('new_trade')
def log_trade(trade):
    price = trade.get('price')
    amount = trade.get('amount')

    money = round(price*amount)


    limit = 0.9

    if amount > limit:
        print(amount)
        #tweettext = "Bitfinex BTCUSD " +  + " USD market bought at "+str(price)
        tweettext2 = "$BTC Bitfinex -> $"+f"{money:,}"+" BOUGHT at $"+str(price)
        print(tweettext2)
        tweet(tweettext2)

    if amount < ((-1)*limit):
        print(amount)
        tweettext2 = "$BTC Bitfinex -> $"+f"{abs(money):,}"+" SOLD at $"+str(price)
        print(tweettext2)
        tweet(tweettext2)

async def start():
  await bfx.ws.subscribe('trades', 'tBTCUSD')

bfx.ws.on('connected', start)
bfx.ws.run()
