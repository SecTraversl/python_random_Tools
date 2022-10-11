import random


# THE PRELIMINARIES


# THE CODE
def get_random(iterable: object, sample_size=10):
    """Creates a random selection list from a given iterable.  Defaults to a 10 item list of samples, but this can changed with the 'sample_size' parameter. 

    Args:
        iterable (object): _description_
        sample_size (int, optional): _description_. Defaults to 10.

    Returns:
        list: Returns a list
    """
    results_list = random.choices(iterable, k=sample_size)
    return results_list


# THE EXECUTION CONTROL
# if __name__ == '__main__':

