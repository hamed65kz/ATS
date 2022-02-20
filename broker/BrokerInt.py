#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

import broker.NobitexTimeResulotion
from broker.OrderBook import OrderBookClass
from tokens.TokenPair import TokenPairClass
from broker.Trades import TradesClass
from tokens.TokenInt import TokenInt
from broker.OHLC import OHLCClass
from broker.OrderResp import OrderRespClass
from broker.OrderType import OrderTypeClass
from broker.ExecutionType import ExecutionTypeClass
from broker.OrderStatus import OrderStatusClass
from broker.OrderListStatus import OrderListStatusClass
from broker.WalletsResp import WalletsRespClass
from broker.Wallet import WalletClass
from broker.NobitexTimeResulotion import NobitexTimeResulotionClass

class BrokerInt(object):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def getOrderBook(TokenPair :TokenPairClass, aDepth=0) -> OrderBookClass:
        """this method is for getting orders list for asks and bids
		@ParamType aTokenPair tokens.TokenPair
		desired token pair symbol
		@ParamType aDepth int
		number of asks/bids from tip of queue
		@ReturnType broker.OrderBook"""
        pass

    @staticmethod
    @abstractmethod
    def getTradesList(aTokenPair : TokenPairClass) -> TradesClass:
        """list last trade of market
		@ParamType aToken tokens.TokenPair
		desired token pair symbol
		@ReturnType broker.Trades"""
        pass

    @staticmethod
    @abstractmethod
    def getMarketState(aSrcCurrency :str, aDstCurrency :str):
        """return last market state
		@ParamType aSrcCurrency tokens.TokenInt
		source currency
		@ParamType aDstCurrency tokens.TokenInt
		destination Currency
		@ReturnType string"""
        pass

    @staticmethod
    @abstractmethod
    def getOHLC(aTokenPair : TokenPairClass, aTimeResolution : NobitexTimeResulotionClass, aStartTime:int, aEndTime:int) -> OHLCClass:
        """get Open-high-low-close with different intervals and different start and end
		@ParamType aTokenPair tokens.TokenPair
		desired token pair symbol
		@ParamType aTimeResolution  string
		time resolution
		@ParamType aStartTime int
		start point unix time
		@ParamType aEndTime int
		end point unix time
		@ReturnType broker.OHLC*"""
        pass

    @staticmethod
    @abstractmethod
    def addOrder(aType: OrderTypeClass, aExecutionType:ExecutionTypeClass , aSrcCurrency : TokenInt, aDstCurrency: TokenInt, aAmount :str, aPrice :str, aStopPrice:str) -> OrderRespClass:
        """register a new order, it returns order id which will be used for monitoring order status
		@ParamType aType broker.OrderType
		indicates sell/buy
		@ParamType aExecutionType broker.ExecutionType
		how to execute the order
		@ParamType aSrcCurrency tokens.TokenInt
		giving currency
		@ParamType aDstCurrency tokens.TokenInt
		requested currency
		@ParamType aAmount string
		srcCurrency volume which we want to exchange to dstCurrency
		@ParamType aPrice string
		unit price of dstCurrency based on srcCurrency
		@ParamType aStopPrice string
		unit price of dstCurrency based on srcCurrency on stop limit price
		@ReturnType broker.OrderResp"""
        pass

    @staticmethod
    @abstractmethod
    def getOrderStatus(aOrderId) -> OrderRespClass:
        """return status of registered order
		@ParamType aOrderId int
		identifier of order
		@ReturnType broker.OrderResp"""
        pass

    @staticmethod
    @abstractmethod
    def getOrdersList(status:OrderListStatusClass,aSrcCurrency : TokenInt, aDstCurrency: TokenInt) -> OrderRespClass:
        pass


    @staticmethod
    @abstractmethod
    def updateOrderStatus(aOrderId, aNewStatus):
        """change order status from new to active or from  active/inactive to cancelled
		@ParamType aOrderId int
		order identifier
		@ParamType aNewStatus broker.OrderStatus
		new order status, it could be used for canceling order
		@ReturnType string"""
        pass

    @staticmethod
    @abstractmethod
    def getProfile():
        """get user profile information
		@ReturnType string"""
        pass

    @staticmethod
    @abstractmethod
    def getWallets() -> WalletsRespClass:
        """return our budget
		@ParamType aTokenSymbol tokens.TokenInt
		symbol of currency
		@ReturnType broker.WalletsResp"""
        pass

    @staticmethod
    @abstractmethod
    def getBalance(aTokenSymbol) -> WalletClass:
        """get budget of one currency in our wallet
		@ParamType aTokenSymbol tokens.TokenInt
		symbol of currency
		@ReturnType broker.Wallet"""
        pass
