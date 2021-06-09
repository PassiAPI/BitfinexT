import tracemalloc
from bfxapi import *


bfx = Client(
  API_KEY="Wkidc8SDrpSLZMbKmSWSlpmbzodzoiP02OVvXoYSvMz",
  API_SECRET="s45h237fbTOB2TY5aHix3iD8fDVaE9XVFpktiaLSKHW"
)


@bfx.ws.on('new_trade')
def log_trade(trade):
  print ("New trade: {}".format(trade))

@bfx.ws.on('connected')
def start():
  bfx.ws.subscribe('trades', 'tBTCUSD')

bfx.ws.run()