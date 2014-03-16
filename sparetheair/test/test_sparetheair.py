#!/usr/bin/env python

import unittest
from datetime import datetime, date
from .. import sparetheair

class SpareTheAirTester(unittest.TestCase):
    def setUp(self):
        self.staUrl = "http://www.eschro.com/stacal/valid.xml"
        self.sta = sparetheair.SpareTheAir(self.staUrl)

    def test_init(self):
        # test valid URLs
        self.assertEqual(self.sta.url, self.staUrl)

        # test invalid URLs
        with self.assertRaises(ValueError):
            sparetheair.SpareTheAir("htneasengoe")
        with self.assertRaises(ValueError):
            sparetheair.SpareTheAir("ftp://test/cant/do/it")
        with self.assertRaises(ValueError):
            sparetheair.SpareTheAir("//test/cant/do/it")
        with self.assertRaises(ValueError):
            sparetheair.SpareTheAir("afp://test/cant/do/it")
        with self.assertRaises(ValueError):
            sparetheair.SpareTheAir("host:/test/cant/do/it")


    def test___getStaStatus(self):
    	# test valid messages
    	self.assertEqual(self.sta.today, datetime(2014, 3, 15, 0, 0))

		# TODO: test invalid messages
        

    # TODO: def test___getMessageFromStaRss(self):


# TODO: class StaCalTester(unittest.TestCase):
#     def test_init(self):

#     def test_write(self):

#     def test___createcal__(self):

#     def test_addToday(self):



if __name__ == '__main__':
    unittest.main()
