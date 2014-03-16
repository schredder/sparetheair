#!/usr/bin/env python

import unittest
from .. import sparetheair

class SpareTheAirTester(unittest.TestCase):
    def setUp(self):
        self.staUrl = "http://www.baaqmd.gov/Feeds/AlertRSS.aspx"
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


    # def test___getStaStatus(self):
        

    # def test___getMessageFromStaRss(self):


# class StaCalTester(unittest.TestCase):
#     def test_init(self):

#     def test_write(self):

#     def test___createcal__(self):

#     def test_addToday(self):



if __name__ == '__main__':
    unittest.main()