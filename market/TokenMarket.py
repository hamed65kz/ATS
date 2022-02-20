#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.OrderListStatus import OrderListStatusClass
from tokens.TokenPair import TokenPairClass
from broker.BrokerInt import BrokerInt
from broker.OrderType import OrderTypeClass
from broker.ExecutionType import ExecutionTypeClass
from broker.OrderStatus import OrderStatusClass
from broker.OrderBook import OrderBookClass
from broker.Order import OrderClass
from broker.NobitexTimeResulotion import NobitexTimeResulotionClass
import threading;
import time;
from datetime import datetime


class TokenMarketClass(object):
    def getOrderBook(self):
        """@ReturnType broker.OrderBook"""
        return self._orderBook

    def getLastTrades(self):
        """@ReturnType broker.Order*"""
        return self._lastTrades

    def marketUpdater(self):
        while True:
            # call broker method for update market
            today = int(datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0, 0, 0).timestamp())
            now = int(datetime.now().timestamp())
            # candles=self._broker.getOHLC(self._token,NobitexTimeResulotionClass.ONE_HOUR,today,now)

            # orderresp=self._broker.addOrder(OrderTypeClass.BUY,ExecutionTypeClass.LIMIT, self._tokenpair.getMainCoin(),
            #        self._tokenpair.getPriceCoin(), "11.35", "265100", "")

            # self._broker.getProfile()

            # self._broker.getBalance(self._tokenpair.getMainCoin())
            # self._broker.getOrderStatus(orderresp.getOrder().getId())
            # if orderresp.getStatus()=='ok':
            #     self._broker.updateOrderStatus(orderresp.getOrder().getId(),OrderStatusClass.CANCELED)
            self._broker.getOrdersList(OrderListStatusClass.OPEN, self._tokenpair.getMainCoin(),
                                       self._tokenpair.getPriceCoin())
            time.sleep(5);

    def __init__(self, tokenPair: TokenPairClass, broker: BrokerInt):
        self._tokenpair = tokenPair
        # @AssociationType tokens.TokenPair
        # @AssociationMultiplicity 1
        self._broker: BrokerInt = broker
        # @AssociationType broker.BrokerInt
        # @AssociationMultiplicity 1
        self._orderBook = None
        """@AttributeType broker.OrderBook"""
        self._lastTrades = None
        """@AttributeType broker.Order*
		list of last trades"""
        try:
            t1 = threading.Thread(target=self.marketUpdater)
            t1.start()
        except:
            print("unable to start market thread")
