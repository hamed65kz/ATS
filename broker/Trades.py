#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.Order import OrderClass
from broker.OrderType import OrderTypeClass
class TradesClass(object):
	def getStatus(self):
		"""@ReturnType string"""
		return self._status

	def getTradesList(self):
		"""@ReturnType broker.Order*"""
		return self._tradesList

	def getTokenPairSym(self):
		return self._tokenPair

	def __init__(self,status,trades,tokenPair):
		self._status = status
		"""@AttributeType string
		indicates does request is successful or not"""
		trades_list = []
		for item in trades:
			ordertype=OrderTypeClass.BUY
			if item['type']=='sell':
				ordertype=OrderTypeClass.SELL
			trades_list.append(OrderClass(time= item['time'],price= item['price'],volume= item['volume'],ordertype= ordertype))

		self._tradesList = trades_list
		"""@AttributeType broker.Order*
		list of last trades of market"""
		self._tokenPair = tokenPair
		"""symbol of token pair"""

