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

    def getLastTrade(self)->OrderClass:
        if self._tradesList is None:
            return None
        return self._tradesList[0]

    def __init__(self, status, trades, tokenPair):
        self._status = status
        """@AttributeType string
		indicates does request is successful or not"""
        broker = 'Nobitex'
        if "isBuyerMaker" in trades[0]:
            broker = 'Binance'

        trades_list = []
        if broker == 'Nobitex':
            for item in trades:
                ordertype = OrderTypeClass.BUY
                if item['type'] == 'sell':
                    ordertype = OrderTypeClass.SELL
                trades_list.append(
                    OrderClass(time=item['time'], price=item['price'], volume=item['volume'], ordertype=ordertype))

        elif broker == 'Binance':
            trades.reverse()
            for item in trades:
                ordertype = OrderTypeClass.BUY
                if item['isBuyerMaker'] == True:
                    ordertype = OrderTypeClass.SELL
                trades_list.append(
                    OrderClass(time=item['time'], price=item['price'], volume=item['qty'], ordertype=ordertype))

        self._tradesList = trades_list
        """@AttributeType broker.Order*
		list of last trades of market"""
        self._tokenPair = tokenPair
        """symbol of token pair"""
