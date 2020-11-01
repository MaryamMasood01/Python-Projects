# Name: Maryam Masood

# PROBLEM A
#==========================================
# Purpose: Computes the contracted distance between the two objects.
#
# Input Parameter(s):
# dist - The original distance (in meters) between two objects
# speed - The speed (in meters/second) at which you are travelling relative
# to the two objects
#
# Return Value(s): The contracted distance between the two objects.
#
#==========================================

def length_contract(dist, speed):
    return(dist * ((1 - ((speed ** 2) / ((3 * (10 ** 8)) ** 2))) ** 0.5))


# PROBLEM B
#==========================================
# Purpose: The function:
# - Computes the time, in years, required to traverse the segment as seen by a stationary observer.
# - Computes the time, in years, required to traverse the segment as seen by Bessel.
#
# Input Parameter(s):
# speed - The speed (in meters/second) at which you are travelling relative
#
# Return Value(s): The time required to traverse the segment, as seen by Bessel, in years.
#
#==========================================

def bessel_run(speed):
    print((12 * (3.086 * (10 ** 16))) / (speed * 31557600))
    return(((length_contract((12 * (3.086 * (10 ** 16))), speed)) / speed) / 31557600)

    
# PROBLEM C
#==========================================
# Purpose: The function prints out the string "Who needs loops?" exactly 100 times in a row, once per line, 
# without the use of loops.
#
# Input Parameter(s): None
#
# Return Value(s): None
#
#==========================================

def print_100():
    print_5()
    print_5()
    print_5()
    print_5()

def print_5():
    print_line()
    print_line()
    print_line()
    print_line()
    print_line()

def print_line():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")


