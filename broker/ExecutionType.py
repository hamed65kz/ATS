#!/usr/bin/python
# -*- coding: UTF-8 -*-
from enum import Enum
class ExecutionTypeClass(Enum):
	MARKET='market'
	LIMIT='limit'
	STOP_MARKET='stop_market'
	STOP_LIMIT='stop_limit'
