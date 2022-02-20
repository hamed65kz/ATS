#!/usr/bin/python
# -*- coding: UTF-8 -*-
from broker.Wallet import WalletClass

class WalletsRespClass(object):
	def getStatus(self):
		"""@ReturnType string"""
		return self._status

	def getWalletsList(self):
		"""@ReturnType broker.Wallet"""
		return self._walletsList

	def __init__(self,status,walletslist):
		self._status = status
		"""@AttributeType string
		status of request"""
		self._walletsList = walletslist
		"""@AttributeType broker.Wallet
		list our wallet per each token"""

