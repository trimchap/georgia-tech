#----------------------------------------------------------------------
# LINEAR SEARCH   - O(n)
#
# Takes 2 parameters, a list of strings, and a string and returns the
# index string if it is found in the list or False if it was not found.
# It only searches for exact matches.
#----------------------------------------------------------------------
def linear(lst, element):
    # step through the list and look for element
    for idx in range(len(lst)):
        if lst[idx] == element:
            # element found
            return idx
    return False


# Test Linear
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print("LINEAR SEARCH: ")
print(linear(a_list, 6))
