#!/usr/bin/python
# -*- coding: UTF-8 -*-
from enum import Enum


class OrderListStatusClass(Enum):
    ALL = 'all'
    OPEN = 'open'
    DONE = 'done'
    CLOSE = 'close'
