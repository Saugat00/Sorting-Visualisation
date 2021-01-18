import pdb


#counting Sort Algorithm
def countingSort(unsortedList):
	#initializing variables
	ListFrequency  = []
	NewList = []

	#length of the list
	length  = len(unsortedList)
	#Finding the max number in the list
	Largest_Number = max(unsortedList) + 1

	#finding the least number in the list
	Minimum_Number = min(unsortedList)

	#creating and initializing the list
	for i in range(0, Largest_Number):
		ListFrequency.append(0)
		
	for i in range (Minimum_Number, Largest_Number):
		NewList.append(0)
	
	#counting an array to store the count of each unique object
	for k in range (0, Largest_Number):

		for l in range (length):

			if k == unsortedList[l]:

				ListFrequency[k] += 1
			
	"""
	Modifying the array such that
	each element at each index 
	stores the sum of the previous count
	"""
	for j in range(1, Largest_Number):
		ListFrequency[j] = ListFrequency[j]+ ListFrequency[j-1]


	"""
	Outputting each object 
	from the input sequence 
	and decreasing its count by 1
	"""
	for i in range(length):
		index = unsortedList[i]
		number = ListFrequency[index]-1
		NewList[number]  = index
		ListFrequency[index] -=1
		yield NewList

	