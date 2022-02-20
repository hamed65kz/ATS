#!/usr/bin/python
# -*- coding: UTF-8 -*-
from enum import Enum


class OrderStatusClass(Enum):
    ACTIVE = 'active'
    DONE = 'done'
    INACTIVE = 'inactive'
    CANCELED = 'canceled'
    NEW = 'new'
