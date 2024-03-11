ascii_art = """
     _   _      _ _
    | | | |    | | |
    | |_| | ___| | | ___
    |  _  |/ _ \ | |/ _ \\
    | | | |  __/ | | (_) |
    \_| |_/\___|_|_|\___/
 
    """
print(ascii_art)
import math
secondsperminute = 60
minutesperhour = 60
hoursperday = 24
daysperyear = 365  

seconds_in_year = secondsperminute * minutesperhour * hoursperday * daysperyear

print("Number of seconds in a year:", seconds_in_year)
 
# 1 mile = 63,360 inches
miles = 1
inches_in_mile = miles * 63360

print(" 1 mile =" + inches_in_mile, "inches.")

lab1_division = 10 // 2
print(lab1_division)
# FLOOR DIVISION : The result is a whole number, excluding decimals
lab1_division2 = 10/2
print(lab1_division2)
# REGULAR DIVISION :The number includes decimals

ages = [23, 45, 67, 21, 89]

#  integer division
averageage_floordiv = sum(ages) // len(ages)
print("The average number using integer division is", averageage_floordiv)

#  regular division
averageage_regdiv = sum(ages) / len(ages)
print("The average number using regular division is", averageage_regdiv)
