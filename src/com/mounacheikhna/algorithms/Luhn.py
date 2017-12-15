
def luhn_check(num):
    # transform the number in a list of digits starting backwards (the check digit is at position 0)
    digits = [int(x) for x in reversed(str(num))]

    
    check_sum = sum()