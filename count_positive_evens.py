
#--------------------------------------------------------------------
# take as input a list of integers, and return an integer that is the
# number of list elements that are both positive and even.
#--------------------------------------------------------------------
def count_positive_evens(lst):
    evens = 0
    for i in range(len(lst)):
        if lst[i]>0 and lst[i]%2 == 0:
            evens+=1
    return evens


# Test
print(count_positive_evens([5, 7, 9, 8, -1, -2, -3]))
print(count_positive_evens([2, 4, 6, 8, 10, 12, 15]))
print(count_positive_evens([-2, -4, -6, -8, -10, 1]))