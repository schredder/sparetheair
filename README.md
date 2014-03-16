# sparetheair

A tool to publish SF Bay Area Spare The Air data as an ical

It reads the RSS Feed: http://www.baaqmd.gov/Feeds/AlertRSS.aspx
...and puts it into an iCal file.

I run this daily, copy the iCal file onto a personal web server, and subscribe to it using OS X's and iOS's Calendar

## Usage
Run `bin/sparetheair`

## Requirements
* Tested using Python 2.7.6
* External Modules:
    * requests
    * rfc3987
    * bs4
    * icalendar

## TODO:
* Factor out RSS URL and iCal file to external config file