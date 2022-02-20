#!/usr/bin/python
# -*- coding: UTF-8 -*-
from marketHistory.MarketHistory import MarketHistoryClass
from technicalAnalysis.IndicatorsCalculator import IndicatorsCalculatorClass
from technicalAnalysis.CandleRecognition import CandleRecognitionClass
from tokens.TokenInt import TokenInt

class TechnicalAnalyzerClass(object):
	"""this class calculate and hold technical parameter for each token, we have one object for each token"""
	def __init__(self):
		self.___marketHistory = None
		# @AssociationType marketHistory.MarketHistory
		self.___technicalIndicators = None
		# @AssociationType technicalAnalysis.IndicatorsCalculator
		self.___candleAnalyzer = None
		# @AssociationType technicalAnalysis.CandleRecognition
		self.___token = None
		"""@AttributeType tokens.TokenInt"""

