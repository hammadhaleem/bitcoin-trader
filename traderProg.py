import asyncio
import logging
import time

import exchangeLayer as el
import traderProg
import genconfig as gc


number_of_trades = 10 

@asyncio.coroutine
def TradeWrapper():
	while True:
		free_money  = el.GetFree('currency')

		frozen_money = el.GetFrozen('currency')
		frozen_btc = el.GetFrozen('asset')

		market_price = el.GetMarketPrice('ask')
	
		sell_price = el.GetMarketPrice('ask')
		buy_price  = el.GetMarketPrice('bid')

		if( frozen_money <= 0.001 and frozen_btc <= 0.001):
			print(str(sell_price) + "\t" + str(buy_price))
		else:
			print ("Still frozen asserts")
		yield from asyncio.sleep(gc.Trader.ReIssueDelay)