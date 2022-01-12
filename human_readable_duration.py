""" 
Task:
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

See: https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""

def format_duration(seconds):
    if not seconds: return 'now' #check for the  edgecase

    in_seconds = { #store the units in seconds in a dict for readability and easy debug
    'years': 365*24*60**2,
    'days': 24*60**2,
    'hours': 60**2,
    'minutes': 60,
    'seconds': 1
    }
    
    result = []
    remainder = seconds #the largest unit, year, will be calculated from the seconds and the rest from its remainder
    for unit in in_seconds:
        div = remainder//in_seconds[unit]
        if div != 0:
            #if the amount of unti is 1 we dont need the plural 's' hence unit[:1]
            result.append(f'{div} {unit if div>1 else unit[:-1]}')
        remainder = seconds%in_seconds[unit] #calculate the smaller units with the remainder

    if len(result)==1:
        #if length is one we dont need commas or and
        return f"{result[-1]}"
            
    return f"{', '.join(result[:-1])} and {result[-1]}"