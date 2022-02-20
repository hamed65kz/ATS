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
from broker.nobitex.NobitexUrls import NobitexUrlsClass
import json
import time;

class NobitexClass(BrokerInt.BrokerInt):
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
        NobitexClass._apiToken = token

    @staticmethod
    def getOrderBook(aTokenPair : TokenPairClass, aDepth=0) -> OrderBookClass:
        """this method is for getting orders list for asks and bids
		@ParamType aTokenPair tokens.TokenPair
		desired token pair symbol
		@ParamType aDepth int
		number of asks/bids from tip of queue
		@ReturnType broker.OrderBook"""

        url = NobitexUrlsClass.getOrderBookUrl(aTokenPair.getSymbol())
        response = NobitexClass._http.request("GET", url)
        resp = response.data.decode()
        data = json.loads(resp)

        obc = OrderBookClass(data['status'], data['bids'], data['asks'], aTokenPair, data['lastUpdate'],
                             data['lastTradePrice'])
        return obc

    @staticmethod
    def getTradesList(aTokenPair : TokenPairClass) -> TradesClass:
        """list last trade of market
		@ParamType aToken tokens.TokenPair
		desired token pair symbol
		@ReturnType broker.Trades"""
        url = NobitexUrlsClass.getTradesUrl(aTokenPair.getSymbol())
        response = NobitexClass._http.request("GET", url)
        resp = response.data.decode()
        data = json.loads(resp)
        trades = TradesClass(data['status'], data['trades'], aTokenPair);
        return trades

    @staticmethod
    def getMarketState(aSrcCurrency, aDstCurrency):
        """return last market state
		@ParamType aSrcCurrency tokens.TokenInt
		source currency
		@ParamType aDstCurrency tokens.TokenInt
		destination Currency
		@ReturnType string"""

    @staticmethod
    def getOHLC(aTokenPair: TokenPairClass, aTimeResolution: NobitexTimeResulotionClass, aStartTimestamp : int,
                aEndTimestamp :int) -> [OHLCClass]:
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

        url = NobitexUrlsClass.getOhlcUrl(aTokenPair.getSymbol(), aTimeResolution.value, aStartTimestamp + 1,
                                          aEndTimestamp)
        response = NobitexClass._http.request("GET", url)
        resp = response.data.decode()
        data = json.loads(resp)
        candles = []
        for x in range(len(data['t'])):
            candles.append(OHLCClass(data['t'][x], data['c'][x], data['o'][x], data['h'][x], data['l'][x], data['v'][x],
                                     aTimeResolution))
        return candles

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
        url = NobitexUrlsClass.getAddOrderUrl()
        if NobitexClass._apiToken == '':
            print("Your token is empty!.")
            resp = OrderRespClass(status='failed', code= 'Token is empty',message= 'Token is empty')
            return resp
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
            "content-type": "application/json",
        }
        params = {"type": aType.value, "execution": aExecutionType.value, "srcCurrency": aSrcCurrency.symbol,
                "dstCurrency": aDstCurrency.symbol, "amount": aAmount, "price": aPrice}
        if aExecutionType == ExecutionTypeClass.STOP_LIMIT:
            params = {"type": aType.value, "execution": aExecutionType.value, "srcCurrency": aSrcCurrency.symbol,
                    "dstCurrency": aDstCurrency.symbol, "amount": aAmount, "price": aPrice, "stopPrice": aStopPrice}

        response = NobitexClass._http.request("POST", url, headers=headers, fields=params)
        resp = response.data.decode()
        data = json.loads(resp)
        if data['status']=='ok':
            order=OrderClass()
            order.fill(data["order"])
            resp=OrderRespClass(status=data['status'],order=order)
            return resp
        else:
            resp=OrderRespClass(status= data['status'],code=data['code'],message= data['message'])
            return resp

    @staticmethod
    def getOrderStatus(aOrderId:int) -> OrderRespClass:
        """return status of registered order
		@ParamType aOrderId int
		identifier of order
		@ReturnType broker.OrderResp"""
        url = NobitexUrlsClass.getOrderStatusUrl()
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
            "content-type": "application/json",
        }
        params = {"id": aOrderId}
        response = NobitexClass._http.request("POST", url, headers=headers, fields=params)
        resp = response.data.decode()
        data = json.loads(resp)
        if 'error' in data:
            resp = OrderRespClass(status='failed',message=data['message'])
            return resp
        else:
            order = OrderClass()
            order.fill(data["order"])
            resp = OrderRespClass(status=data['status'], order=order)
            return resp

    def updateOrderStatus(aOrderId:int, aNewStatus:OrderStatusClass)-> OrderRespClass:
        """change order status from new to active or from  active/inactive to cancelled
		@ParamType aOrderId int
		order identifier
		@ParamType aNewStatus broker.OrderStatus
		new order status, it could be used for canceling order
		@ReturnType string"""
        url = NobitexUrlsClass.getOrderUpdateUrl()
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
            "content-type": "application/json",
        }
        params = {"order": aOrderId+1,"status":aNewStatus.value}
        response = NobitexClass._http.request("POST", url, headers=headers, fields=params)
        resp = response.data.decode()
        data = json.loads(resp)
        if 'error' in data:
            resp = OrderRespClass(status='failed', message=data['message'],code=data["error"])
            return resp
        else:
            resp = OrderRespClass(status=data['status'], message=data['updatedStatus'])
            return resp
    @staticmethod
    def getProfile():
        """get user profile information
		@ReturnType string"""
        url=NobitexUrlsClass.getProfileUrl()
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
        }
        response = NobitexClass._http.request("POST", url, headers=headers)
        resp = response.data.decode()
        data = json.loads(resp)
        return data

    @staticmethod
    def getWallets() -> WalletsRespClass:
        """return our budget
		@ParamType aTokenSymbol tokens.TokenInt
		symbol of currency
		@ReturnType broker.WalletsResp"""
        url = NobitexUrlsClass.getWallets()
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
        }
        response = NobitexClass._http.request("POST", url, headers=headers)
        resp = response.data.decode()
        data = json.loads(resp)
        wlist =[]
        for w in data['wallets']:
            wlist.append(WalletClass(w['currency'],w['id'],w['balance'],w['blockedBalance']))
        resp=WalletsRespClass(data['status'],wlist)
        return resp

    @staticmethod
    def getBalance(aToken:TokenInt) -> WalletClass:
        """get budget of one currency in our wallet
		@ParamType aTokenSymbol tokens.TokenInt
		symbol of currency
		@ReturnType broker.Wallet"""
        url = NobitexUrlsClass.getBalanceUrl()
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
        }
        params = {"currency": aToken.symbol}
        response = NobitexClass._http.request("POST", url, headers=headers, fields=params)
        resp = response.data.decode()
        data = json.loads(resp)
        balance=WalletClass(token=aToken,status= data['status'],balance= data['balance'])
        return balance

    @staticmethod
    def getOrdersList(status: OrderListStatusClass, aSrcCurrency: TokenInt,
                      aDstCurrency: TokenInt) -> OrderRespClass:
        url = NobitexUrlsClass.getOrderListUrl()
        headers = {
            "Authorization": f"Token {NobitexClass._apiToken}",
            "content-type": "application/json",
        }
        params = {"status": status.value, "srcCurrency": aSrcCurrency.symbol,
                  "dstCurrency": aDstCurrency.symbol, "detail": 2 }
        response = NobitexClass._http.request("POST", url, headers=headers, fields=params)
        resp = response.data.decode()
        data = json.loads(resp)
        if data["status"]=='failed':
            resp = OrderRespClass(data['status'], message=data['message'],code=data['code'])
            return resp
        ord = []
        for o in data['orders']:
            ordObj=OrderClass()
            ordObj.fill(o)
            ord.append(ordObj)
        resp = OrderRespClass(data['status'], ord)
        return resp
