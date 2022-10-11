import random


# THE PRELIMINARIES


# THE CODE
def new_random_number(string_length=30):
    """Creates a random number string. You can specify the number of digits with the 'string_length' parameter.

    Args:
        string_length (int, optional): Specify a desired number size. Defaults to 30.

    Returns:
        str: Returns a string object that is a number
    """
    
    # The elements will be integers ranging from 0 to 9
    possible_values = list(range(10))
    
    # From the "possible_values" of numbers 0 - 9, there will be multiple random choices, the quantity of which is based off of the number given to "k=" (returns a "k" sized list)
    random_list_of_ints = random.choices(possible_values, k=string_length)
    
    # Then we take that list of random numbers and join them together making one long string of digits
    random_number_string = "".join([str(e) for e in random_list_of_ints])
    return random_number_string


# THE EXECUTION CONTROL
# if __name__ == '__main__':

