'''
Created on 12/09/2012

@author: bpd900
'''

import unittest

import shared


class SharedTests(unittest.TestCase):

	def test_ifg(self):
		ifg = shared.Ifg('../../tests/sydney_test/obs/geo_060619-061002.unw')
