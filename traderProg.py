import asyncio
import logging
import time

import exchangeLayer as el
import traderProg
import genconfig as gc
import time 

number_of_trades = 20
diff = 0.012

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
		to_issue_trades = get_trades( market_price, market_price , number_of_trades , free_money , free_coin )
		if( frozen_money <= 0.001 and frozen_btc <= 0.001):
			for trades in to_issue_trades : 
				try:
					if (trades[0] < 0 ):
						el.Trade('buy' , trades[1] , trades[0] * - 1 )
					else: 
						el.Trade('sell' , trades[1] , trades[0]  )
				except Exception as e :
					print("[Exception]\t Exception: Unable to issue trade for : " + str(trades))
			try:
				val = (float(el.GetFree('currency')) + float(el.GetFrozen('currency'))) + (float(el.GetFree('asset')) + float(el.GetFrozen('asset'))) * float(el.GetMarketPrice('ask'))
				print("[Info]\tFree Money :{0:5}\tFree Coin :{1:5}\tAsserts :{2:5}\tMarket price :{3:5}".format(el.GetFree('currency') , el.GetFree('asset') , val ,el.GetMarketPrice('ask'))) 
			except Exception as e :
				pass
		else:
			try:
				val = (float(el.GetFree('currency')) + float(el.GetFrozen('currency'))) + (float(el.GetFree('asset')) + float(el.GetFrozen('asset'))) * float(el.GetMarketPrice('ask'))
				print("[Wait]\tFree Money :{0:5}\tFree Coin :{1:5}\tAsserts :{2:5}\tMarket price :{3:5}".format(el.GetFree('currency') , el.GetFree('asset') , val ,el.GetMarketPrice('ask'))) 
			except Exception as e :
				print ("[Skipping]\t\tStill frozen asserts\r"),
				pass
			time.sleep(5)
		yield from asyncio.sleep(gc.Trader.ReIssueDelay)