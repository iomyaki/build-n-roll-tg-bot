import random


def select_random_from_list(arr):
    if len(arr) == 0:
        return None
    return arr[random.randint(0, len(arr) - 1)]
