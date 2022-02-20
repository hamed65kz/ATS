#!/usr/bin/python
# -*- coding: UTF-8 -*-
import SecretsHolder
from traders.Trader import TraderClass
from tokens.TokenPair import TokenPairClass
from strategies.StrategyA import StrategyAClass;
from traders.Asset import AssetClass;
from broker.nobitex.Nobitex import NobitexClass;
from market.TokenMarket import TokenMarketClass;
from technicalAnalysis.TechnicalAnalyzer import TechnicalAnalyzerClass;


class MainClass:
    traders=[];
    def run(self, aToken_list,secretkey):
        """@ParamType aToken_list tokens.TokenPair*"""

        asset = AssetClass();  # it should update itself and then go to next line
        NobitexClass.setApiToken(SecretsHolder.SecretsHolderClass.getPlainKey())

        for t in aToken_list:
            market =  TokenMarketClass(t, NobitexClass);
            ta = None;  #TechnicalAnalyzer(t);
            strg_a =  StrategyAClass(market,ta);
            tr = TraderClass(t, strg_a, asset, NobitexClass);
            self.traders.append(tr);


    def __init__(self):
        self.___traders = None
    # @AssociationType traders.Trader*

