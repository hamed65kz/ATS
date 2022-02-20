#!/usr/bin/python
# -*- coding: UTF-8 -*-
from enum import Enum
class NobitexTimeResulotionClass(Enum):
	ONE_HOUR = '60'
	THREE_HOUR = '180'
	SIX_HOUR = '360'
	TWLEVE_HOUR = '720'
	ONE_DAY = 'D'
	TWO_DAY = '2D'
	THREE_DAY = '3D'
