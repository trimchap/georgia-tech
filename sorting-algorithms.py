#---------------------------------------------
# Bubble Sort - runs in an O(n^2)
#--------------------------------------------- 
def sort_with_bubbles(lst):
    swap_occurred = True
    
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

    return lst

#Test
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print('Bubble Sort :',sort_with_bubbles([5, 3, 1, 2, 4]))

#---------------------------------------------
# Selection Sort - runs in an O(n^2)
#--------------------------------------------- 
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

# Test Selection Sort
print('Selection Sort:')
list_to_sort = [2,5,3,8,6,9,1,4,7]
selection_sort(list_to_sort)