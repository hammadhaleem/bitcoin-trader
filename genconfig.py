import genconfig


class API:
  Verbose = True
  Exchange = 'okcoin'
  TradePair = 'btc_cny'
  Asset = TradePair[:3]
  Currency = TradePair[-3:]
  apikey = 'f1930abf-2a84-4547-8837-577667e62391'
  secretkey = 'AA57DC97A64AA09A0514FEF1CD891550'
  AssetTradeMin = 0.01

class Trader:
  Enabled = True
  Verbose = True
  ReIssueDelay = 1 
 