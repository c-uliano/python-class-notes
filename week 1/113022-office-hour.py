"""
* type in a date to figure out what day of the week it is
* if statements, and variables, and 1 other thing that we'll need to look up to complete this
? https://www.almanac.com/how-find-day-week#:~:text=Take%20the%20last%20two%20digits,digits%20(discard%20any%20remainder).&text=Divide%20the%20sum%20by%207,the%20day%20of%20the%20week
so what day of the week was December 26, 2004?
todo: last 2 digits of the year: 04
todo: add 1/4 of those digits to that, discard remainder: 1
04 + 1 = 05
todo: add to that the day of the month & the month key number
January = 1 …leap year = 0 February = 4 …leap year = 3 March = 4 April = 0 May = 2 June = 5 July = 0 August = 3 September = 6 October = 1 November = 4 December = 6
05 + 26 + 6 = 37
todo: divide by 7, the remainder is the day
todo: if the year is between 2000-2099 subtract 1 before dividing
sunday = 1 monday = 2 tuesday = 3 wednesday = 4 thursday = 5 friday = 6 saturday = 0
37 - 1 = 36
36 / 7 = 5.1 ... so it's a Sunday
"""

import math

# ? the year, slice the last 2 digits, make sure the final working product is an integer
fullYear = 2004
year = str(fullYear)[2:5]
year = int(year)
# print(year)
# print(type(year))

# ? a quarter of the year, discarded remainder
quarterIt = year / 4
quarterIt = math.floor(quarterIt)
# print(quarterIt)

# ? add year and quarterIt together
yearAndQuarter = year + quarterIt
print(yearAndQuarter)

month = 'december'
dayOfMonth = 26
monthKeys = {
    'january': 1,
    'januaryLeapYear': 0,
    'february': 4,
    'februaryLeapYear': 3,
    'march': 4,
    'april': 0,
    'may': 2,
    'june': 5,
    'july': 0,
    'august': 3,
    'september': 6,
    'october': 1,
    'november': 4,
    'december': 6
}

total = yearAndQuarter + dayOfMonth
# ! how do you loop through a dictionary?
for i in range():
    pass