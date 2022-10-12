import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# THE PRELIMINARIES


# THE CODE
def new_random_words_list(list_size=10):
    """Creates a list of randomly generated words derived from the API of 'https://random-word-api.herokuapp.com'.

    Args:
        list_size (int, optional): Specify the number of words. Defaults to 10.

    Returns:
        list: Returns a list of random words
    """
    url = f'https://random-word-api.herokuapp.com/word?number={list_size}'
    with requests.Session() as s:
        response = s.get(url, json={}, verify=False)
    return response.json()


# THE EXECUTION CONTROL
# if __name__ == '__main__':

