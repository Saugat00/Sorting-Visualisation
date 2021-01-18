import pdb


#Applying MergeSort algorithm 
def mergeList(left_List, right_List):

    #initializing some variable
    i = 0
    j = 0
    sortedList = [] 

    #Calculates the length of left and right index in the list 
    Length_Left = int(len(left_List))
    Length_Right = int(len(right_List))

    #Start merging array back till complete arrray is arranged
    while(i < Length_Left) and (j < Length_Right):

        if left_List[i] <= right_List[j]:
            sortedList.append(left_List[i])
            i += 1
        else:
            sortedList.append(right_List[j])
            j +=1

    while(i < Length_Left):

        sortedList.append(left_List[i])
        i +=1
    while(j < Length_Right):

        sortedList.append(right_List[j])
        j +=1
    #pdb.set_trace()

def mergeSort(unsortedList):

    length = int(len(unsortedList))

    #finding the middle index to divide the array into two halves
    midIndex = int(length /2)

    #stores the element from 0 index to MidIndex
    left_List = unsortedList[:midIndex]

    #stores the element from MidIndex to the end in list
    right_List = unsortedList[midIndex:]

    #setting up the base case
    if (length <2):
        return

    else:
        #applying divide and concor process by recursive call   
        yield from  mergeSort(left_List)
        yield from mergeSort(right_List)
        #pdb.set_trace()
        yield from mergeList(left_List, right_List)