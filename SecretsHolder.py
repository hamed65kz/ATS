#!/usr/bin/python
# -*- coding: UTF-8 -*-
class SecretsHolderClass(object):
    Encryptedkey = '';

    def __init__(self, Encryptedkey):
        self.Encryptedkey = Encryptedkey;

    @staticmethod
    def getPlainKey():
        return 'cab7dc349466f95191ad7bc11ab3cf94231717ef';

