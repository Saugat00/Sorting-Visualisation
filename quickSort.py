
#This function swaps the given number
def swap(unsortedList, i, j):

    #Swapping the provided numbers
    unsortedList[i],unsortedList[j] = unsortedList[j],unsortedList[i]


#This function does the recursive partitaion
def partation(unsortedList, left, right): 

    #Here i always shows the last of the index that is less then pivot
    i = ( left-1 )
    #making the last index as pivot
    pivotIndex = unsortedList[right]     # pivot 
    #assuming that last index is sorted so decreasing right index by 1
    for j in range(left , right): 
  
        # If current element is smaller than the pivot 
        if   unsortedList[j] < pivotIndex: 
          
            # This increases the index of smaller element 
            i +=1 
            swap(unsortedList, i, j) 
    #this code will store pivot in between of left and right
    swap(unsortedList, i+1, right)
#This is the main recursive algorithm for quicksort
def quickSort(unsortedList, left, right):


    #this condition will determine if the loop is complete
    if (left > right):
        return
    else:

        #Calling the pivot function and storing the index of pivot
        #pdb.set_trace()

        pivotIndex =  partation(unsortedList, left, right)

        #Recursive sorting the left_side numbers from pivot
        yield from quickSort(unsortedList, left, pivotIndex-1)
         
        #Recursive sorting the right_side numbrs from pivot
        yield from quickSort(unsortedList, pivotIndex+1, right)
         
