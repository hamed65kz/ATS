#!/usr/bin/python
# -*- coding: UTF-8 -*-
from strategies.StrategyInt import StrategyInt

class StrategyAClass(StrategyInt):
	@classmethod
	def __init__(self,market,ta):
		self.___market = market
		# @AssociationType market.TokenMarket
		# @AssociationMultiplicity 1
		self.___technicalAnalyzer = ta
# @AssociationType technicalAnalysis.TechnicalAnalyzer

