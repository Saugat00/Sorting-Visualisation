import pdb

"""
This function will swap the 
given two index from the list
 """
def swap(unsortedList, i, j):

    #Swapping the provided numbers
    unsortedList[i],unsortedList[j] = unsortedList[j],unsortedList[i]


def selectionSort(unsortedList):
	length = len(unsortedList)
	#loop from starting to the end of the list
	for i in range (length -1):

		#Assuming i as sorted numbers of index in the list
		sortedIndex = i
		#This loop will compare the current index with index of smallest number
		for j in range(sortedIndex+1,length):
			
			"""
			Changing the index number of smallestNumberIndex
			and making sure if that number is smallest
			if not then changing the index number
			"""
			if(unsortedList[sortedIndex] > unsortedList[j]):
				sortedIndex = j
				yield unsortedList
		"""
		This loop is checking if i is the smallest number
		if not then calling the swap function
		"""
		if sortedIndex != i:
			swap(unsortedList, i, sortedIndex)
			yield unsortedList
	#Pdb is a debugging tool for python
	#pdb.set_trace()

	#this will return the final sortedList 
	yield unsortedList