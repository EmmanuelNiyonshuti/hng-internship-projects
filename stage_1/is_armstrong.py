"""
An Armstrong number (Narcissistic number) is a number
that is equal to the sum of its digits raised
to the power of the number of digits.
"""
def is_armstrong(n):
    """
    check is a number is armstrong.
    """
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n
