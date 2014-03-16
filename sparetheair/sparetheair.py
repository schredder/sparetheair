#!/usr/bin/env python

import requests, sys, os, re, rfc3987
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from icalendar import Calendar, Event


class SpareTheAir:
    def __init__(self, url):
        if (rfc3987.match(url, 'URI') == None or not re.match("^http(s)?://.*", url)):
            raise ValueError('Invalid URL')
        else:
            self.url = url
            self.__getStaStatus(self.__getMessageFromStaRss())

    def __getStaStatus(self, info):
        (day, message) = info

        today = date(date.today().year, day.month, day.day)
        if (re.match('.*([nN]o){0}.*Alert ([nN]ot ){0}In Effect.*', message) \
            and not re.match('.*No Alert.*', message)):
            inEffect = True
        else: inEffect = False

        self.today = day
        self.inEffect = inEffect
        self.message = message

        return (day, inEffect)

    def __getMessageFromStaRss(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        divs = soup.find_all(class_='aq12')
        builddate = soup.find('date')
        day = datetime.strptime(builddate.text, '%A, %B %d, %Y')
        
        message = builddate.find_next_sibling('description').text
        if message == None: raise ValueError('RSS Message is empty.')
        return (day, message)

class StaCal:
    def __init__(self, stacalfile, staURL):
        self.__stacalfile = stacalfile
        self.__staURL = staURL
        self.__createcal()

    # Save the calendar to disk
    def writeToCalFile(self):
        try:
            with open(self.__stacalfile, 'w') as vcal:
                vcal.write(self.calendar.to_ical())
        except IOError:
            sys.stderr.write('Unable to write to %s' % self.__stacalfile)

    # Open the calendar if it exists, or create it if it doesn'b
    def __createcal(self):
        try:
            with open(self.__stacalfile, 'r') as vcal:
                self.calendar = Calendar.from_ical(vcal.read())
        except IOError:
            # init the calendar...
            self.calendar = Calendar()
            self.calendar.add('prodid', '-//SpareTheAir Cal - ESS//eschro.com//')
            self.calendar.add('version', '2.0')

    def addtoday(self):
        def eventFilter(e):
            e.get('dtstart').dt == date.today() \
            and e.get('summary') == 'Spare The Air Alert In Effect'

        sta = SpareTheAir(self.__staURL)
        
        # only add event if STA is in effect and today hasn't already been added
        todaysEvents = filter(eventFilter, self.calendar.subcomponents)
        if sta.inEffect and not todaysEvents:
            today = Event()
            today.add('summary', 'Spare The Air ' + sta.message)
            today.add('dtstart', sta.today.date())
            today.add('dtend', sta.today.date() + timedelta(days=1))
            self.calendar.add_component(today)

def main(argv):
    #sta = SpareTheAir('http://www.baaqmd.gov/Feeds/AlertRSS.aspx')
    #print '%s: %s' % (sta.today, sta.message)
    stacal = StaCal('stacal.ics', 'http://www.baaqmd.gov/Feeds/AlertRSS.aspx')
    stacal.addtoday()
    stacal.writeToCalFile()


if __name__ == '__main__':
    main(sys.argv)
