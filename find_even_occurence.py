




import time

# http://www.ardendertat.com/2011/12/13/programming-interview-questions-22-find-odd-occurring-element/
# given an integer array, one element occurs odd number of times and all others have even occurrences
# find the element with odd occurrences

# todo: make faster!
# note: this might speed up with the knowledge that only ONE element occurs an odd number of times...
# note: probably an easy way to do this with linear search time, though i wonder how...



def findEvenOccurence(array):
	
	# create empty dictionary for counts
	dictionary = {}

	# iterate through each element in array
	# if in dictionary, add 1; else, store as 1
	for element in array:
		if element not in dictionary: dictionary[element] = 1
		else: dictionary[element] += 1

	# iterate through the dictionary, keeping track of whether even or odd (as measured by modulos), if odd, then print that value
	for key, value in dictionary.iteritems():
		if value % 2 == 1: continue
		else: print key



# example use case
list1 = [2, 2, 2, 2, 2, 5, 5, 5, 10, 10, 12, 12, 12, 12, 12, 14, 14, 14, 9, 9, 9, 9, 9]



# debugging
startTime = time.time()
findEvenOccurence(list1)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"





