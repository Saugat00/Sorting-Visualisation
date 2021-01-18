import pdb
#This function swaps the given number
def swap(unsortedList, i, j):

	unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i]

#applying InsertionSort Algorithm
def insertionSort(unsortedList):

	length = len(unsortedList)
	#iterating form first index to the end
	for i in range (0, length):
		for j in range (i, -1, -1):
			#This compares current key to its predecessor
			if (unsortedList[i]< unsortedList[j]):

				#calling swap function
				swap(unsortedList, i, j)
				j -= 1
				i -=1

				yield unsortedList
