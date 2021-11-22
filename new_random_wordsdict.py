# %%
#######################################
def new_random_wordsdict(listsize=10):
    """Returns a dictionary of random words, where the key is a numeric value starting at 0 and the value is the word.  The default size of the initial random word list is 10, but this can be modified with the "listsize" parameter.

    Example:
        >>> new_random_wordsdict()\n
        {0: 'justifying', 1: 'respondents', 2: 'woolier', 3: 'oscillating', 4: 'dispossession', 5: 'Huns', 6: 'radiogram', 7: 'leaping', 8: "Scala's", 9: 'stamens'}

    Args:
        listsize (int, optional): Specify the desired length of the list. Defaults to 10.

    Returns:
        dict: Returns a dictionary of words.
    """
    import random
    word_file = "/usr/share/dict/words"
    with open(word_file) as f:
        content = f.readlines()
        results_list = random.choices(content, k=listsize)
        # Removes the trailing '\n' line feed character
        results_list = [w.strip() for w in results_list]
    results_dict = {i: results_list[i] for i in range(len(results_list))}
    return results_dict

