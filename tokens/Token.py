#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tokens.TokenInt import TokenInt


class TokenClass(TokenInt):

    def __init__(self, sym, fullname):
        self.symbol = sym;
        self.fullname = fullname;
