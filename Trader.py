import asyncio
import time
import Trader 
import exchangeLayer as el
import genconfig as gc
import traderProg as trd
import Trader 

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  
  if el.AdditionalAsync:
    for i in el.AdditionalAsync:
      asyncio.async(i)
  if gc.Trader.Enabled:
    asyncio.async(trd.TradeWrapper())
  loop.run_forever()