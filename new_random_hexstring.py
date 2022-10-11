import random


# THE PRELIMINARIES


# THE CODE
def new_random_hexstring(string_length=32):
    """Creates a pseudo-random hexadecimal string.
    
    References:
        - This was helpful:  https://stackoverflow.com/questions/45220221/python-random-hex-generator

    Args:
        string_length (int, optional): Specify the length of the string. Defaults to 32.

    Returns:
        str: Returns a string containing valid hexadecimal characters
    """
    results = []
    for _ in range(string_length):
        results.append(random.choice('0123456789abcdef'))
    return ''.join(results)


# THE EXECUTION CONTROL
# if __name__ == '__main__':

