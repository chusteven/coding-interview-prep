




import time

# there is an array of non-negative integers
# a second array is formed by shuffling the elements of the first array and deleting a random element
# given these two arrays, find which element is missing in the second array
# note: may be duplicates so figure out which is missing

# todo: make runtime better
# http://www.ardendertat.com/2011/09/27/programming-interview-questions-4-find-missing-element/



def findMissingElement(originalArray, shuffledArray):



	"""
	# the following method uses dictionaries
	firstArray = {}
	for element in originalArray:
		if element not in firstArray: firstArray[element] = 1
		elif element in firstArray: firstArray[element] += 1

	secondArray = {}
	for element in shuffledArray:
		if element not in secondArray: secondArray[element] = 1
		elif element in secondArray: secondArray[element] += 1

	# then find out all the same key values pairs that are equivalent and then keep the one that isn't the same...
	"""

	# sorts arrays and stores them
	originalArray.sort()
	shuffledArray.sort()

	# zipping does the following - creates tuples of first, second, third, ..., nth elements in all the lists inputted
	# note: that if the number of elements doesn't line up, then it simple cuts off after the m-n(th) element - see below for example case
	for num1, num2 in zip(originalArray, shuffledArray):

		# note that becasue these are shuffled, the first time the tuples don't line up, we have our mismatch
		# in this situation, we know that num1 (element of the original list) is the one that's missing
		# so return this value
		if num1 != num2: return num1

	# if things match up perfectly the entire way, just return the last element (no particular reason)
	return originalArray[-1]



# example use case
firstArray = [4, 1, 0, 2, 9, 6, 8, 7, 5, 3]
secondArray = [6, 4, 7, 2, 1, 0, 8, 3, 9]



# debugging + tracking time
startTime = time.time()
print findMissingElement(firstArray, secondArray)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"








