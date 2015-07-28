#
# Everything below is fully documented in
# http://galts-gulch.github.io/avarice/configuring
#
import genconfig


class API:
  Verbose = True
  Exchange = 'okcoin'
  TradePair = 'btc_cny'
  Asset = TradePair[:3]
  Currency = TradePair[-3:]
  apikey = '9cd5ad93-ce6f-4ed2-9bf7-0edf97763526'
  secretkey = '977FB94C7A351154720B16F12F6C4883'
  AssetTradeMin = 0.01

class Trader:
  Enabled = True
  Verbose = True
  ReIssueDelay = 1 
 