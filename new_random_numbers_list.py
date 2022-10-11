import random


# THE PRELIMINARIES


# THE CODE
def new_random_numbers_list(list_size=10, min_num=0, max_num=1000):
    """Returns a list of pseudo-random numbers.  The default size of the list is 10, but this can be modified with the "list_size" parameter.

    Args:
        list_size (int, optional): Specify the desired length of the list. Defaults to 10.
        min_num (int, optional): Specify the lowest number. Defaults to 0.
        max_num (int, optional): Specify the highest number. Defaults to 1000.

    Returns:
        list: Returns a list of integers.
    """
    results_list = []
    for i in range(list_size):
        rand_num = random.randint(min_num, max_num)
        results_list.append(rand_num)
    return results_list


# THE EXECUTION CONTROL
# if __name__ == '__main__':

