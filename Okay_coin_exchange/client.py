#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

# apikey，secretkey,url
apikey = 'f1930abf-2a84-4547-8837-577667e62391'
secretkey = 'AA57DC97A64AA09A0514FEF1CD891550'
okcoinRESTURL = 'www.okcoin.com'

# https://github.com/OKCoin/rest

# API
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)

# API
okcoinFuture = OKCoinFuture(okcoinRESTURL, apikey, secretkey)

print (u' Spot market')
print (okcoinSpot.ticker('btc_usd'))

print (u' Spot depth')
print (okcoinSpot.depth('btc_usd'))

# Print ( u ' spot market ' )
# print (okcoinSpot.trades())

# print (u' 用户现货账户信息 ')
# print (okcoinSpot.userinfo())

# print (u' 现货下单 ')
# print (okcoinSpot.trade('ltc_usd','buy','0.1','0.2'))

# print (u' 现货批量下单 ')
# print (okcoinSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

# print (u' 现货取消订单 ')
# print (okcoinSpot.cancelOrder('ltc_usd','18243073'))

# print (u' 现货订单信息查询 ')
# print (okcoinSpot.orderinfo('ltc_usd','18243644'))

# print (u' 现货批量订单信息查询 ')
# print (okcoinSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

# print (u' 现货历史订单信息查询 ')
# print (okcoinSpot.orderHistory('ltc_usd','0','1','2'))

# print (u' 期货行情信息')
# print (okcoinFuture.future_ticker('ltc_usd','this_week'))

# print (u' 期货市场深度信息')
# print (okcoinFuture.future_depth('btc_usd','this_week','6'))

# print (u'期货交易记录信息')
# print (okcoinFuture.future_trades('ltc_usd','this_week'))

# print (u'期货指数信息')
# print (okcoinFuture.future_index('ltc_usd'))

# print (u'美元人民币汇率')
# print (okcoinFuture.exchange_rate())

# print (u'获取预估交割价')
# print (okcoinFuture.future_estimated_price('ltc_usd'))

# print (u'获取全仓账户信息')
# print (okcoinFuture.future_userinfo())

# print (u'获取全仓持仓信息')
# print (okcoinFuture.future_position('ltc_usd','this_week'))

# print (u'期货下单')
# print (okcoinFuture.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

# print (u'期货批量下单')
# print (okcoinFuture.future_batchTrade('ltc_usd','this_week',
# '[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

# print (u'期货取消订单')
# print (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

# print (u'期货获取订单信息')
# print (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))

# print (u'期货逐仓账户信息')
# print (okcoinFuture.future_userinfo_4fix())

# print (u'期货逐仓持仓信息')
# print (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))
