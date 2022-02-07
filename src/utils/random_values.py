import random
import string


def create_rand_string(len_string):
    if len_string < 1:
        raise Exception('String should have at least 1 symbol')

    rand_string = string.ascii_letters
    # rand_string = string.ascii_lowercase
    rand_string = ''.join(random.choice(rand_string) for i in range(len_string))
    return rand_string
