#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
from datetime import datetime, date
import sys

class SpareTheAir:
    def __init__(self, url):
        self.url = url
        self.__getStaStatus()

    def __getStaStatus(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        divs = soup.find_all(class_='aq12')

        day = datetime.strptime(divs[0].text, "%A, %m/%d")
        today = date(date.today().year, day.month, day.day)
        inEffect = (True if divs[2].text == "in Effect" else False)

        self.today = today
        self.inEffect = inEffect

        return (today, inEffect)

def main(argv):
    sta = SpareTheAir('http://www.baaqmd.gov/Feeds/BurnStatusIframe.aspx')
    print "On %s, a spare the air day is in effect: %s" % (sta.today, sta.inEffect)


if __name__ == '__main__':
    main(sys.argv)