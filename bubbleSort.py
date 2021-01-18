
import pdb

#This function swaps the given number
def swap(unsortedList, j):
	#compares current key to the next key in the list
	if unsortedList[j] > unsortedList[j+1]:				
				unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
	return (unsortedList)

#Applying BubbleSort Algorithm
def bubbleSort(unsortedList):
	length = len(unsortedList) -1
	i = 0
	j = 0
	flag = False

	"""pdb.set_trace()"""
	#This iterates till the end of list
	while flag == False:
		flag = True
		for j in range (length):
				#calling swap function
				swap(unsortedList, j)
				flag = False
				
				yield unsortedList

		#As we know last number of index is always sorted in every iteration
		length = length -1

		#reseting the loop after the each iteration of list
		j = 0
