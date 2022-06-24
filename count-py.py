#!/usr/bin/env python3

import time
import itertools

min = 0
hour = 0
day = 0
week = 0
year = 0
sec = -1
secToYear = -1

YN = ''
WN = ''
DN = ''
HM = ''
MN = ''
SN = ''

for i in itertools.count(0):
   sec = sec + 1
   secToYear = secToYear + 1
   if sec > 59:
      sec = 0
      min = min + 1

   if min > 59:
      min = 0
      hour = hour + 1

   if hour > 23:
      hour = 0
      day = day + 1

   if day > 6:
      day = 0
      week = week + 1

   if secToYear > 31557600:
      secToYear = 0
      week = 0
      year = year + 1


   if sec == 1:
      S = 'Second '
   else:
      S = 'Seconds'

   if min == 1:
      M = 'Minute '
   else:
      M = 'Minutes'

   if hour == 1:
      H = 'Hour '
   else:
      H = 'Hours'

   if day == 1:
      D = 'Day '
   else:
      D = 'Days'

   if week == 1:
      W = 'Week '
   else:
      W = 'Weeks'

   if year == 1:
      Y = 'Year '
   else:
      Y = 'Years'


   if sec > 9:
      SN = ''
   else:
      SN = ' '

   if min > 9:
      MN = ''
   else:
      MN = ' '

   if hour > 9:
      HN = ''
   else:
      HN = ' '

   if week > 9:
      WN = ''
   else:
      WN = ' '

   if year > 9:
      YN = ''
   else:
      YN = ' '

   print('   ', year, Y, YN, ' ⎜ ', week, W, WN, ' ⎜ ', day, D, DN, ' ⎜ ', hour, H, HN, ' ⎜ ', min, M, MN, ' ⎜ ', sec, S, SN, ' ⎜ ', secToYear, 'Total Seconds', '   ')
   time.sleep(1)

