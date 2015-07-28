import asyncio
import logging
import time

import exchangeLayer as el
import traderProg
import genconfig as gc
import time 

number_of_trades = 10
diff = 0.05

def get_trades( sell_price , buy_price,  parts , free_money , free_coin):
	if ( sell_price == None or buy_price == None):
		return []
	sell_price = sell_price + diff
	buy_price =  buy_price - diff
	trades = []
	for i in range(1 , parts + 1):
		in_hand_money = -1 * ( free_money / parts ) 
		in_hand_coin = free_coin / parts 
		coin_buy = (round(in_hand_money / (buy_price - ( diff * i )),3) , round(buy_price - ( diff * i ) , 3) )
		coin_sell = (round(in_hand_coin,3)  , round(sell_price + ( diff * i ) , 3) )
		trades.append(coin_buy)
		trades.append(coin_sell)
	return trades

@asyncio.coroutine
def TradeWrapper():
	while True:
		free_money  = el.GetFree('currency')
		free_coin   = el.GetFree('asset')

		frozen_money = el.GetFrozen('currency')
		frozen_btc = el.GetFrozen('asset')

		market_price = el.GetMarketPrice('ask')
	
		sell_price = el.GetMarketPrice('ask')
		buy_price  = el.GetMarketPrice('bid')
		if( frozen_money <= 0.001 and frozen_btc <= 0.001):
			to_issue_trades = get_trades( market_price, market_price , number_of_trades , free_money , free_coin )

			#(coin , price ) -ve means buy
			# Trade(order, rate, amount):
			# print (to_issue_trades)
			for trades in to_issue_trades : 
				# print(trades)
				try:
					if (trades[0] < 0 ):
						print("[Buy]\t" + str(el.Trade('buy' , trades[1] , trades[0] * - 1 )))
					else: 
						print("[Sell]\t" + str(el.Trade('sell' , trades[1] , trades[0]  )))
				except Exception as e :
					print("[Exception]\t Exception: Unable to issue trade " + str(trades))
		else:
			print ("[Skipping]\t\tStill frozen asserts")
		time.sleep(5)
		yield from asyncio.sleep(gc.Trader.ReIssueDelay)
