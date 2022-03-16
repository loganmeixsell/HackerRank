def birthdayCakeCandles(ar):
    birthmax = max(ar)
    total = 0
    for x in ar:
        if x == birthmax:
            total += 1
    return total





birthdays = [1,5,3,6,4,6]
birthdayCakeCandles(birthdays) 