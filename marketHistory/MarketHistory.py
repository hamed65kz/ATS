#!/usr/bin/python
# -*- coding: UTF-8 -*-
from marketHistory.HistoryFetcher import HistoryFetcherClass
from tokens.TokenInt import TokenInt

class MarketHistoryClass(object):
	def __init__(self):
		self.___dataFetcher = None
		# @AssociationType marketHistory.HistoryFetcher
		self.___token = None
		"""@AttributeType tokens.TokenInt"""

