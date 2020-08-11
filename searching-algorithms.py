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

#----------------------------------------------------------------------
# BINARY SEARCH   - O(logn)
#
# Takes a list and a search term and returns True if the term is found 
# in the list and False if not
#----------------------------------------------------------------------
def binary_search(searchList, searchTerm):

    # the list must be sorted
    searchList.sort()
    
    min = 0
    max = len(searchList) - 1
    
    # loop through while there is 1 term or more in the list
    while min <= max:
        print("Searching for", searchTerm, "in", searchList[min:max+1])
        
        # Find the middle - use integer math
        currentMiddle = (min + max) // 2

        if searchList[currentMiddle] == searchTerm:
            return True             # term found
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1 # term is less than middle, throw away right half
        else:
            min = currentMiddle + 1 # term is greater than middle, throw away left half

    # term not found in list
    return False

# Test BINARY SEARCH
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in list:", binary_search(intlist, 23))
print("--")
print("50 is in list:", binary_search(intlist, 50))
print("--")
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in list:", binary_search(strlist, "David"))
print("--")
print("Lucy is in list:", binary_search(strlist, "Lucy"))
print("--")
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in list:", binary_search(datelist, date(1885, 10, 13)))
print("--")
print("11/28/2015 is in list:", binary_search(datelist, date(2015, 11, 28)))
print("--")