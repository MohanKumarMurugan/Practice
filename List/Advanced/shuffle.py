# Implement a function to shuffle a list randomly.

import random

def shuffle_list(input_list):

    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

original_list = [1, 2, 3, 4, 5]
shuffled = shuffle_list(original_list)
print("Original List:", original_list)
print("Shuffled List:", shuffled)