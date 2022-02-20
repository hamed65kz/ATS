#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.OrderBook import OrderBook
from tokens.TokenPair import TokenPair
from broker.Trades import Trades
from tokens.TokenInt import TokenInt
from broker.OHLC import OHLC
from broker.OrderResp import OrderResp
from broker.OrderType import OrderType
from broker.ExecutionType import ExecutionType
from broker.OrderStatus import OrderStatus
from broker.WalletsResp import WalletsResp
from broker.Wallet import Wallet
from broker.BrokerInt import BrokerInt

class BinanceClass(BrokerInt):
	def getOrderBook(self, aTokenPair, aDepth = 0):
		"""this method is for getting orders list for asks and bids
		@ParamType aTokenPair tokens.TokenPair
		desired token pair symbol
		@ParamType aDepth int
		number of asks/bids from tip of queue
		@ReturnType broker.OrderBook"""
		pass

	def getTradesList(self, aToken):
		'list last trade of market'
		pass

	def getMarketState(self, aSrcCurrency, aDstCurrency):
		'return last market state'
		pass

	def getOHLC(self, aTokenPair, aTimeResolution_, aStartTime, aEndTime):
		'get Open-high-low-close with different intervals and different start and end'
		pass

	def addOrder(self, aType, aExecutionType, aSrcCurrency, aDstCurrency, aAmount, aPrice, aStopPrice):
		'register a new order, it returns order id which will be used for monitoring order status'
		pass

	def getOrderStatus(self, aOrderId):
		'return status of registered order'
		pass

	def updateOrderStatus(self, aOrderId, aNewStatus):
		'change order status from new to active or from  active/inactive to cancelled'
		pass

	def getProfile(self):
		'get user profile information'
		pass

	def getWallet(self, aTokenSymbol):
		'return our budget'
		pass

	def getBalance(self, aTokenSymbol):
		'get budget of one currency in our wallet'
		pass

