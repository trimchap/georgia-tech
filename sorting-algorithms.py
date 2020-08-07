#---------------------------------------------
# Bubble Sort - runs in an O(n^2)
#--------------------------------------------- 
def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True
    
    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:
        
        #Start off assuming a swap did not occur
        swap_occurred = False
        
        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them!
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                swap_occurred = True

    return lst

#Test
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print('bubble sort :',sort_with_bubbles([5, 3, 1, 2, 4]))