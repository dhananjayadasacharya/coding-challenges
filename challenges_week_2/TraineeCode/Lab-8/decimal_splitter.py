class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    def get_fraction(number):
        return round(number - int(number), 2)

    """
    Method to check if a given number is odd or even
    """
    def is_odd(number):
        return number&1
