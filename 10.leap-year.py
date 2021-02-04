"""
Given a year, report if it is a leap year.
https://exercism.io/tracks/python/exercises/leap/

The tricky thing here is that a leap year in the Gregorian calendar occurs:
    on every year that is evenly divisible by 4
      except every year that is evenly divisible by 100
        unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.
"""

def is_leap(year):
    "Return True if the inuput year is leap"
    if (year % 100 == 0 and year % 400 != 0) or year % 4 != 0:
        return False
    return True
 

if __name__ == "__main__":
    while True:
        try:
            user_input = int(input("Enter a year: "))
            break
        except ValueError:
            print("You haven't enter an integer, try again!")
    if(is_leap(user_input)):
        print(f"{user_input} is a leap year.")
    else:
        print(f"{user_input} is NOT a leap year.")