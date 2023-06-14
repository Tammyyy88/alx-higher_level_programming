#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store elements present in only one set
    different_set = set()
    # Iterate over each element in the first set
    for element in set_1:
        # Check if the element is not present in the second set
        if element not in set_2:
            # If it is not, add the element to the different set
            different_set.add(element)
    # Iterate over each element in the second set
    for element in set_2:
        # Check if the element is not present in the first set
        if element not in set_1:
            # If it is not, add the element to the different set
            different_set.add(element)
    return different_set
