# %%
#######################################
def new_random_wordslist(listsize=10):
    """Returns a list of random words.  The default size of the list is 10, but this can be modified with the "listsize" parameter.

    Example:
        >>> new_random_wordslist()\n
        ['Botswana', "lymphoma's", 'forwarder', 'curatives', "Anshan's", 'temporary', "Rorschach's", "superconductor's", 'parents', "analysis's"]

    Args:
        listsize (int, optional): Specify the desired length of the list. Defaults to 10.

    Returns:
        list: Returns a list of words.
    """
    import random
    word_file = "/usr/share/dict/words"
    with open(word_file) as f:
        content = f.readlines()
        results_list = random.choices(content, k=listsize)
        # Removes the trailing '\n' line feed character
        results_list = [w.strip() for w in results_list]
        return results_list

