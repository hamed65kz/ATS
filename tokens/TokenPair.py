#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tokens.TokenInt import TokenInt

class TokenPairClass(object):
	def getMainCoin(self)->TokenInt:
		"""@ReturnType tokens.TokenInt"""
		return self._mainCoin

	def getPriceCoin(self)->TokenInt:
		"""@ReturnType tokens.TokenInt"""
		return self._priceCoin
	def getSymbol(self):
		return self._symbol

	def __init__(self,tokenMain:TokenInt,tokenPrice:TokenInt,symbol):
		self._symbol = symbol
		"""@AttributeType string
		token pair symbol like btcusd, it include two currency"""
		self._mainCoin = tokenMain
		# @AssociationType tokens.TokenInt
		# """the main coin which we trade"""
		self._priceCoin = tokenPrice
		"""@AttributeType tokens.TokenInt
		the coin which we show the main coin price based on that"""

