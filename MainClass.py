#!/usr/bin/python
# -*- coding: UTF-8 -*-
import SecretsHolder
from traders.Trader import TraderClass
from tokens.TokenPair import TokenPairClass
from strategies.StrategyA import StrategyAClass
from traders.Asset import AssetClass
from broker.nobitex.Nobitex import NobitexClass
from broker.binance.Binance import BinanceClass
from market.TokenMarket import TokenMarketClass
from technicalAnalysis.TechnicalAnalyzer import TechnicalAnalyzerClass
from telegram.telegram import TelegramClientClass


class MainClass:
    traders = [];

    def run(self, aToken_list, secretkey):
        """@ParamType aToken_list tokens.TokenPair*"""
        # TelegramClientClass.connect()
        asset = AssetClass()  # it should update itself and then go to next line
        NobitexClass.setApiToken(SecretsHolder.SecretsHolderClass.getPlainKey())

        for t in aToken_list:
            binancemarket = TokenMarketClass(t[1], BinanceClass)
            nobitexmarket = TokenMarketClass(t[0], NobitexClass)
            ta = None  # TechnicalAnalyzer(t)
            strg_a = StrategyAClass(nobitexmarket,binancemarket, ta)
            tr = TraderClass(t, strg_a, asset, NobitexClass)
            self.traders.append(tr)

    def __init__(self):
        self.___traders = None
    # @AssociationType traders.Trader*
