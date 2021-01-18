import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import bubbleSort
import mergeSort
import quickSort
import selectionSort
import countingSort
import insertionSort
import sys

#creating the random unsorted list
def random_Number(unsortedList, number):
	#user input for range of number for list

	
	
	#loop from 0 to user input number 
	for i in range(1, number):
	
		#generates the random number form 1 to range number
		numberGenerator  = random.randint(1, number)
		unsortedList.append(numberGenerator)

	print (unsortedList)
	print("\n")

	return (unsortedList)
#initializing the list
unsortedList = []

#Command line menu for user input
Algorithm = int(input("Please Choose the Algorithm you want to sort the numbers with:\n"\
 "   1. Bubble_Sort\n \
  2. Merge_sort\n \
  3. Quick_Sort\n \
  4. Selection_Sort\n \
  5. Insertion_Sort\n \
  6. Counting_Sort\n \
  7. Exit \n"))
#user input for number range to create random number
number = int(input("Please enter the numbers you want for sorting: "))
random_Number(unsortedList, number)


"""
Checking user choice of sorting algorithm
and Calling sorting Algorithm
"""
if (Algorithm == 1):
	title = "Bubble_Sort"
	Algorithm = bubbleSort.bubbleSort(unsortedList)

	#print unsortedList
elif (Algorithm == 2):
	title = "Merge_Sort"
	Algorithm = mergeSort.mergeSort(unsortedList)
elif (Algorithm == 3):
	title = "Quick_Sort"
	length = len(unsortedList)
	#sets the left and right index at the begining
	left = 0
	right = length-1

	#Calling quicksort function
	Algorithm = quickSort.quickSort(unsortedList,left,right)
elif (Algorithm == 4):
	title = "Selection_Sort"
	Algorithm = selectionSort.selectionSort(unsortedList)

elif (Algorithm == 5):
	title = "Insertion_Sort"
	Algorithm = insertionSort.insertionSort(unsortedList)
	
elif (Algorithm == 6):
	title = "Counting_Sort"
	Algorithm = countingSort.countingSort(unsortedList)
elif(Algorithm ==7):
	sys.exit()



# This initializes the figure
fig, ax = plt.subplots()
ax.set_title(title)

bar_rec = ax.bar(range(len(unsortedList)), unsortedList, align='edge')

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

ax.set_xlim(0, number)
ax.set_ylim(0, int(number * 1.1))


epochs = [0]

#updates the graph 
def update_plot(unsortedList, rec, epochs):
    for rec, val in zip(rec, unsortedList):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))


anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=Algorithm, interval=1, repeat=False)
plt.show()





