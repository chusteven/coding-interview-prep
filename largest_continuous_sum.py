




import time

# given an array of integers (positive and negative) find the largest continuous sum
# todo: integrate into one function where i can better understand what's happening at every step of the way...



# this is a helper function to calculate the running sum of a particular element
def findContSum(array):

	# define empty list to be populated with running sums
	sums = []

	# iterate through each index of this list
	for i in range(len(array)):

		# prints every element of that array up to that particular index
		# print "index:", i, "array:", array[:i+1]

		# prints the running sum of these arrays
		# print sum(array[:i+1])

		# calculate running sum, append to list of sums
		runningSum = sum(array[:i+1])
		sums.append(runningSum)

	return sums



# debugging
# print findContSum([3, 6, 5, 1, 10, 8])



# this is the actual function
def largestContinuousSum(array):

	# define current maximum
	maxSum = 0

	# iterate through all indices of the array 
	for i in range(len(array)):

		# grab the current array as specified by index
		currentArray = array[i:]

		# grab array of continuous sums using helper function, find maximum of this array
		currentSums = findContSum(currentArray)
		maxCurrentSum = max(currentSums)

		# check to see if bigger than max, if so store it
		if maxCurrentSum > maxSum: 
			maxSum = maxCurrentSum

			# for investigating what's happening purposes...
			print "index:", i
			print "max sum:", maxSum

	return maxSum



# example use case
# print largestContinuousSum([3, 6, 5, 1, 10, 8])
# print largestContinuousSum([4, -5, 10, -12, 3, 43, -9, 31, 0, 1, 4, 20, -10, -20, 33, 4, 27])



# debugging + tracking time
startTime = time.time()
print largestContinuousSum([4, -5, 10, -12, 3, 43, -9, 31, 0, 1, 4, 20, -10, -20, 33, 4, 27])
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"





# raw method:

# 3
# 3+6
# 3+6+5
# 3+6+5+1
# 3+6+5+1+10
# 3+6+5+1+10+8

# 6
# 6+5
# 6+5+1
# 6+5+1+10
# 6+5+1+10+8

# 5
# 5+1
# 5+1+10
# 5+1+10+8

# 1
# 1+10
# 1+10+8

# 10
# 10+8

# 8



