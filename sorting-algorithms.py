#----------------------------------------------------------------------
# BUBBLE SORT    - runs in an O(n^2)
#
# Go through the list and compare items 2 at a time. If they are in 
# the wrong order, swap them. Go through the list again comparing 
# and swapping until there are no more swaps.
#----------------------------------------------------------------------
def sort_with_bubbles(lst):
    swap_occurred = True
    print(lst)
    
    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:
        swap_occurred = False
        
        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]: # swap needed?
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                swap_occurred = True
                print(lst)

    return lst

# Test BUBBLE SORT
print('BUBBLE SORT :')
sort_with_bubbles([2,5,3,8,6,9,1,4,7])

#----------------------------------------------------------------------
# SELECTION SORT    - runs in an O(n^2)
#
# Look through the list for the lowest element and move it to the front.
# Then look through the remaining list and move the next lowest element 
# to the front. Repeat for the length of the list.
#----------------------------------------------------------------------
def selection_sort(lst):

    # start the sort at the beginning of the list
    next_start = 0 
    print(next_start,':',lst)

    while next_start < len(lst):
        min_index = next_start
        for i in range(next_start,len(lst)):
            if lst[i] < lst[min_index]:
                # find the lowest value in the list
                min_index = i
            i+=1
        # swap the lowest value with the start of the list
        lst[next_start],lst[min_index] = lst[min_index],lst[next_start]
        # move the index one to the right - all items to the left are now sorted
        next_start+=1 
        print(next_start,':',lst)

# Test SELECTION SORT
print('SELECTION SORT:')
list_to_sort = [2,5,3,8,6,9,1,4,7]
selection_sort(list_to_sort)


#----------------------------------------------------------------------
# INSERTION SORT    - runs in an O(n^2)
#
# Step through the unsorted list and if the next item is out of order,
# insert it in the correct order of the items we have already sorted .
#----------------------------------------------------------------------
def insertion_sort(lst):
    
    print(lst)
    # sort the first two
    if lst[0] > lst[1]:
        lst[0],lst[1] = lst[1],lst[0]
    print(lst)
    next_idx = 2

    # then go through each element from the 3rd to the end and move it to the sorted side
    while next_idx < len(lst):
        sort_me = next_idx
        # move the sort_me element left until it's correctly sorted
        while sort_me > 0:
            if lst[sort_me] < lst[sort_me - 1]:
                lst[sort_me],lst[sort_me - 1] = lst[sort_me - 1],lst[sort_me] # swap
                print(lst)
                sort_me-=1
            else:
                sort_me = 0 # done. this element is sorted now
        next_idx+=1

# Test INSERTION SORT
print('INSERTION SORT:')
list_to_sort = [5,2,3,8,6,9,1,4,7]
insertion_sort(list_to_sort)


#----------------------------------------------------------------------
# MERGE SORT   - nlogn
#
# Break the list into lists of length one then merge adjacent lists
# (left and right) recursively in sorted order
#----------------------------------------------------------------------

def mergesort(lst):

    # if the list has only one item return
    if len(lst) <= 1:
        return lst
    else:
        # split the list into 2 and call mergesort on the left and right sides
        middle = len(lst)//2 # return an integer
        # sort the left side and sort then right side - recursive
        left = mergesort(lst[:middle])
        right = mergesort(lst[middle:])
        print(left)
        print(right)

        newlist = []
        # while both lists are not of zero length
        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                # add the lowest left to the new list and delete from left
                newlist.append(left[0])
                del left[0]
            else:
                # add the lowest right to the new list and delete from right
                newlist.append(right[0])
                del right[0]

        # one of these lists is empty, the other is sortend and added to the end
        newlist.extend(right)
        newlist.extend(left)

        return newlist


# Test MERGE SORT
print('MERGE SORT')
print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))
#
# Other sorts: shell sort, heap sort, quick sort
#