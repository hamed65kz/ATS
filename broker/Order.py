#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.OrderType import OrderTypeClass
from broker.OrderStatus import OrderStatusClass
from tokens.TokenInt import TokenInt


class OrderClass(object):
    def getPrice(self):
        """@ReturnType string"""
        return self._price

    def getVolume(self):
        """@ReturnType string"""
        return self._volume

    def getType(self):
        """@ReturnType broker.OrderType"""
        return self._type

    def getTime(self):
        """@ReturnType string"""
        return self._time

    def getTotalPrice(self):
        """@ReturnType string"""
        return self._totalPrice

    def getId(self):
        """@ReturnType int"""
        return self._id

    def getFee(self):
        """@ReturnType int"""
        return self._fee

    def getSrcCurrency(self):
        """@ReturnType tokens.TokenInt"""
        return self._srcCurrency

    def getDstCurrency(self):
        """@ReturnType tokens.TokenInt"""
        return self._dstCurrency

    def getUnmatchedAmount(self):
        """@ReturnType string"""
        return self._unmatchedAmount

    def getMatchedAmount(self):
        """@ReturnType string"""
        return self._matchedAmount

    def getPartial(self):
        """@ReturnType boolean"""
        return self._partial

    def getExecution(self):
        return self._execution

    def __init__(self, price:str =0, volume:str =0, ordertype:OrderTypeClass = None, time:int = 0):
        self._price = price
        self._volume = volume
        self._type = ordertype;
        self._time = time
        self._totalPrice = 0
        self._id = 0
        self._fee = 0
        self._orderStatus = ''
        self._srcCurrency = ''
        self._dstCurrency = ''
        self._unmatchedAmount = ''
        self._matchedAmount = ''
        self._partial = ''
        self._execution = ''

    def fill(self, order:dict):
        if 'price' in order :
            self._price = order['price']
        if 'amount' in order :
            self._volume = order['amount']
        if 'type' in order :
            self._type = order['type']
        if 'created_at' in order:
            self._time = order['created_at']
        if 'totalOrderPrice' in order:
            self._totalPrice = order['totalOrderPrice']
        if 'id' in order :
            self._id = order['id']
        if 'fee' in order:
            self._fee = order['fee']
        if 'status' in order:
            self._orderStatus = order['status']
        if 'srcCurrency' in order:
            self._srcCurrency = order['srcCurrency']
        if 'dstCurrency' in order:
            self._dstCurrency = order['dstCurrency']
        if 'unmatchedAmount' in order:
            self._unmatchedAmount = order['unmatchedAmount']
        if 'matchedAmount' in order:
            self._matchedAmount = order['matchedAmount']
        if 'partial' in order:
            self._partial = order['partial']
        if 'execution' in order :
            self._execution = order['execution']
