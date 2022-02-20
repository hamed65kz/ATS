#!/usr/bin/python
# -*- coding: UTF-8 -*-
class OHLCClass(object):
	def getOpen(self):
		"""@ReturnType string"""
		return self._open

	def getHigh(self):
		"""@ReturnType string"""
		return self._high

	def getLow(self):
		"""@ReturnType string"""
		return self._low

	def getClose(self):
		"""@ReturnType string"""
		return self._close

	def getStatus(self):
		"""@ReturnType string"""
		return self._status

	def getStartTime(self):
		"""@ReturnType float"""
		return self._startTime

	def getVolume(self):
		"""@ReturnType string"""
		return self._volume

	def getDuration_min(self):
		"""@ReturnType int"""
		return self._duration_min

	def __init__(self,time,close,open,high,low,vol,duration):
		self._open = open
		"""@AttributeType string
		token open price"""
		self._high = high
		"""@AttributeType string
		token high price"""
		self._low = low
		"""@AttributeType string
		token low price"""
		self._close = close
		"""@AttributeType string
		token close price"""

		self._startTime = time
		"""@AttributeType float
		start of interval time"""
		self._volume = vol
		"""@AttributeType string
		volume of trades in this interval"""
		self._duration = duration
		"""@AttributeType int
		duration of interval based on minute"""

