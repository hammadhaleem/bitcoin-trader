import asyncio
import time

import avarice
import exchangeLayer as el
import genconfig as gc
import traderProg as trd
import Trader 

# RunAll automatically if avarice is run directly
if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  
  if el.AdditionalAsync:
    for i in el.AdditionalAsync:
      asyncio.async(i)
  if gc.Trader.Enabled:
    asyncio.async(trd.TradeWrapper())
  loop.run_forever()
