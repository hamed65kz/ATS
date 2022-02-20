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

	def traderHandler():
		while True:
			print('trader do something from trader thread');
			time.sleep(1);

	def __init__(self, aToken, aStrategy, aAsset, aBroker):
		"""@ParamType aToken tokens.TokenPair
		@ParamType aStrategy strategies.StrategyInt
		@ParamType aAsset traders.AssetClass
		@ParamType aBroker broker.BrokerInt"""
		self.___tokenpair = aToken
		# @AssociationType tokens.TokenPair
		# @AssociationMultiplicity 1
		self.___strategyInt = aStrategy
		# @AssociationType strategies.StrategyInt
		# @AssociationMultiplicity 1
		self.___asset = aAsset
		# @AssociationType traders.AssetClass
		self.___broker = aBroker
		# @AssociationType broker.BrokerInt

		try:
			t1 = threading.Thread(target=TraderClass.traderHandler)
			t1.start()
		except:
			print("unable to start trader thread")




