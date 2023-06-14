#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted keys of the dictionary
    sorted_keys = sorted(a_dictionary.keys())
    # Iterate over the sorted keys and print the key-value pairs
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
