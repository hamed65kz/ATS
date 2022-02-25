#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tokens.TokenPair import TokenPairClass
from strategies.StrategyInt import StrategyInt
from traders.Asset import AssetClass
from broker.BrokerInt import BrokerInt
import threading;
import time;
class TraderClass(object):

	def start(self):
		pass

	def stop(self):
		pass

	def traderHandler(self):
		while True:
			self.__strategy.doAnalyze()
			#print('trader do something from trader thread : ' + str(int(time.time())));

			time.sleep(5);

	def __init__(self, aToken, aStrategy, aAsset, aBroker):
		"""@ParamType aToken tokens.TokenPair
		@ParamType aStrategy strategies.StrategyInt
		@ParamType aAsset traders.AssetClass
		@ParamType aBroker broker.BrokerInt"""
		self.__tokenpair = aToken
		# @AssociationType tokens.TokenPair
		# @AssociationMultiplicity 1
		self.__strategy :StrategyInt = aStrategy
		# @AssociationType strategies.StrategyInt
		# @AssociationMultiplicity 1
		self.__asset = aAsset
		# @AssociationType traders.AssetClass
		self.__broker = aBroker
		# @AssociationType broker.BrokerInt

		try:
			t1 = threading.Thread(target=self.traderHandler())
			t1.start()
		except Exception as ex:
			print("unable to start trader thread " + str(ex))




