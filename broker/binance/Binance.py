#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.OrderBook import OrderBookClass
from tokens.TokenPair import TokenPairClass
from broker.Trades import TradesClass
from tokens.TokenInt import TokenInt
from broker.OHLC import OHLCClass
from broker.OrderResp import OrderRespClass
from broker.Order import OrderClass
from broker.OrderType import OrderTypeClass
from broker.ExecutionType import ExecutionTypeClass
from broker.OrderStatus import OrderStatusClass
from broker.WalletsResp import WalletsRespClass
from broker.NobitexTimeResulotion import NobitexTimeResulotionClass
from broker.OrderListStatus import OrderListStatusClass
from broker.Wallet import WalletClass
from broker import BrokerInt
import urllib3
from broker.binance.BinanceUrls import BinanceUrlsClass
import json
import time;

class BinanceClass(BrokerInt.BrokerInt):
    _oRDERBOOK_LIMIT = 60
    """@AttributeType int
	nobitex has 60 request per minutes limit for getting orderbook"""
    _tRADESLIST_LIMIT = 15
    """@AttributeType int
	nobitex has 15 request per minutes limit for getting trades list, it return last 20 trade"""
    _sTATE_LIMIT = 10
    """@AttributeType int
	market state request limit, nobitex has 100 request per 10 minutes limitation"""
    _aDD_ORDER_LIMIT = 10
    """order limit is 100 request per 10 minutes"""
    _oRDER_STATUS_LIMIT = None
    """@AttributeType int
	get order status has 60 request per a minute limitation"""
    _uPDATE_STATUS_LIMIT = 30
    """Nobitex has 30 update request per minute limitation"""

    _http = urllib3.PoolManager()
    _apiToken = ''

    @staticmethod
    def setApiToken(token:str):
        BinanceClass._apiToken = token

    @staticmethod
    def getOrderBook(aTokenPair : TokenPairClass, aDepth=0) -> OrderBookClass:
        """this method is for getting orders list for asks and bids
		@ParamType aTokenPair tokens.TokenPair
		desired token pair symbol
		@ParamType aDepth int
		number of asks/bids from tip of queue
		@ReturnType broker.OrderBook"""
        pass

    @staticmethod
    def getTradesList(aTokenPair : TokenPairClass) -> TradesClass:
        """list last trade of market
		@ParamType aToken tokens.TokenPair
		desired token pair symbol
		@ReturnType broker.Trades"""
        url = BinanceUrlsClass.getTradesUrl(aTokenPair.getSymbol())
        response = BinanceClass._http.request("GET", url)
        resp = response.data.decode()
        data = json.loads(resp)
        trades = TradesClass('ok', data, aTokenPair);
        return trades

    @staticmethod
    def getMarketState(aSrcCurrency, aDstCurrency):
        """return last market state
		@ParamType aSrcCurrency tokens.TokenInt
		source currency
		@ParamType aDstCurrency tokens.TokenInt
		destination Currency
		@ReturnType string"""
        pass

    @staticmethod
    def getOHLC(aTokenPair: TokenPairClass, aTimeResolution: NobitexTimeResulotionClass, aStartTimestamp : int,
                aEndTimestamp :int) -> [OHLCClass]:
        pass

    @staticmethod
    def addOrder(aType: OrderTypeClass, aExecutionType: ExecutionTypeClass, aSrcCurrency: TokenInt,
                 aDstCurrency: TokenInt, aAmount: str, aPrice: str, aStopPrice: str) -> OrderRespClass:
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
    def getOrderStatus(aOrderId:int) -> OrderRespClass:
        """return status of registered order
		@ParamType aOrderId int
		identifier of order
		@ReturnType broker.OrderResp"""
        pass

    def updateOrderStatus(aOrderId:int, aNewStatus:OrderStatusClass)-> OrderRespClass:
        """change order status from new to active or from  active/inactive to cancelled
		@ParamType aOrderId int
		order identifier
		@ParamType aNewStatus broker.OrderStatus
		new order status, it could be used for canceling order
		@ReturnType string"""
        pass
    @staticmethod
    def getProfile():
        """get user profile information
		@ReturnType string"""
        pass

    @staticmethod
    def getWallets() -> WalletsRespClass:
        """return our budget
		@ParamType aTokenSymbol tokens.TokenInt
		symbol of currency
		@ReturnType broker.WalletsResp"""
        pass

    @staticmethod
    def getBalance(aToken:TokenInt) -> WalletClass:
        """get budget of one currency in our wallet
		@ParamType aTokenSymbol tokens.TokenInt
		symbol of currency
		@ReturnType broker.Wallet"""
        pass

    @staticmethod
    def getOrdersList(status: OrderListStatusClass, aSrcCurrency: TokenInt,
                      aDstCurrency: TokenInt) -> OrderRespClass:
        pass
