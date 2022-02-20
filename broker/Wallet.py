#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tokens.TokenInt import TokenInt


class WalletClass(object):
    """special currency wallet/balance"""

    def getToken(self):
        """@ReturnType tokens.TokenInt"""
        return self._token

    def getId(self):
        """@ReturnType int"""
        return self._id

    def getBalance(self):
        """@ReturnType string"""
        return self._balance

    def getBlocked(self):
        """@ReturnType string"""
        return self._blocked

    def getStatus(self):
        """@ReturnType string"""
        return self._status

    def __init__(self, token, id=0, balance=0, block=0, status=""):
        self._token = token
        self._id = id
        self._balance = balance
        self._blocked = block
        self._status = status
