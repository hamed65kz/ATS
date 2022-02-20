#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.Order import OrderClass


class OrderRespClass(object):
    """status of order related requests"""

    def getStatus(self):
        """@ReturnType string"""
        return self._status

    def getOrder(self):
        """@ReturnType broker.Order"""
        return self._order

    def getErrorCode(self):
        """@ReturnType string"""
        return self._errorCode

    def getErrorMessage(self):
        """@ReturnType string"""
        return self._errorMessage

    def __init__(self, status: str, order: OrderClass = None, code="", message=""):
        self._status = status
        """@AttributeType string
		status of add order request"""
        self._order = order
        """@AttributeType broker.Order
		order detail"""
        self._errorCode = code
        """@AttributeType string
		code of error on failed request"""
        self._errorMessage = message
        """@AttributeType string
		message of error"""
