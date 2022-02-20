#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.Order import OrderClass
from tokens.TokenPair import TokenPairClass
from broker.OrderType import OrderTypeClass;
class OrderBookClass(object):
	def getStatus(self):
		"""@ReturnType string"""
		return self._status

	def getBids(self):
		"""@ReturnType broker.Order*"""
		return self._bids

	def getAsks(self):
		"""@ReturnType broker.Order*"""
		return self._asks

	def getTokenPairSym(self):
		"""@ReturnType tokens.TokenPair"""
		return self._tokenPairSym

	def getLastTradePrice(self):
		return self._lastTradePrice;

	def getLastUpdateTime(self):
		return self._lastUpdateTime;

	def __init__(self,status,bids,asks,tokenPair,lastUpdateTime,lastTradePrice):
		self._status = status
		"""	request success or failed"""
		bids_list=[]
		for item in bids :
			bids_list.append(OrderClass(price=item[0],volume= item[1],ordertype= OrderTypeClass.SELL))

		self._bids = bids_list
		"""list of sell orders"""
		asks_list=[]
		for item in asks :
			asks_list.append(OrderClass(price= item[0], volume=item[1],ordertype=OrderTypeClass.BUY))
		self._asks = asks_list
		"""list of buy orders"""
		self._tokenPair = tokenPair
		"""symbol of orderbook token pair"""

		self._lastUpdateTime = lastUpdateTime
		self._lastTradePrice = lastTradePrice

