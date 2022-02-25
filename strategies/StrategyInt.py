#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from market.TokenMarket import TokenMarketClass
from technicalAnalysis.TechnicalAnalyzer import TechnicalAnalyzerClass

class StrategyInt(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def doAnalyze(self):
        pass


