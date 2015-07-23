import asyncio
import logging
import time

import exchangeLayer as el
import traderProg
import genconfig as gc

buy_pool = []
sell_pool = []
@asyncio.coroutine
def TradeWrapper():
	while True:
	  	print(el.GetFree('currency'))
	  	print(el.GetFrozen('currency'))
	  	print(el.GetMarketPrice('ask'))
	  	print (buy_pool)
	  	print (sell_pool)

	  	buy_pool.append(el.GetMarketPrice('ask'))
	  	sell_pool.append(el.GetMarketPrice('bid'))
	  	yield from asyncio.sleep(gc.Trader.ReIssueDelay)