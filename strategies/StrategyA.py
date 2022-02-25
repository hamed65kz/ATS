#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from strategies.StrategyInt import StrategyInt
from market.TokenMarket import TokenMarketClass
class StrategyAClass(StrategyInt):
	@classmethod
	def __init__(self,nobitexmarket,binancemarket,ta):
		self.__nobitexMarket : TokenMarketClass = nobitexmarket
		self.__binanceMarket : TokenMarketClass = binancemarket
		# @AssociationType market.TokenMarket
		# @AssociationMultiplicity 1
		self.__technicalAnalyzer = ta

	def doAnalyze(self):
		nobitexlasttrade= self.__nobitexMarket.getLastTrade()
		binancelasttrade = self.__binanceMarket.getLastTrade()
		if nobitexlasttrade is None:
			print('wait for nobitex')
			return
		if binancelasttrade is None:
			print('wait for binance')
			return

		txt = "{nobitex:.10}, {binance:.10} , {time} , {sym}".format(nobitex=nobitexlasttrade.getLastTrade().getPrice(),
																	 binance=binancelasttrade.getLastTrade().getPrice(),
																	 time = int(time.time()),
																	 sym = "BTCUSDT")
		f = open("pricehistory.txt", "a")
		f.writelines('\n'+txt)
		f.close()
		print('Nobitex = '+nobitexlasttrade.getLastTrade().getPrice() + "  ,Binance = " + ('%.10s' % binancelasttrade.getLastTrade().getPrice())+' , sym = BTCUSDT , time = '+ str(int(time.time())))
# @AssociationType technicalAnalysis.TechnicalAnalyzer

