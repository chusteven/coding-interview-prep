




import time

# 3. Maximum Difference

# Given an array of integer elements, a subsequence of this array is a set of consecutive elements from the array (ie: given the array v: [7, 8, -3, 5, -1], a subsequence of v is [8, -3, 5])

# Your task is to write a function that finds a left and a right subsequence of the array that satisfy the following conditions
# - the two subsequences are unique (they don't have shared elements)
# - the difference between the sum of the elements in the right subsequence and the sum of the elements in the left subsequence is maximum
        
# Print the difference to the standard output (stdout)

# Note that your function will receive the following arguments:
# - v, which is the array of integers

# Data constraints:
# - the array has at least 2 and at most 1,000,000 numbers
# - all the elements in the array are integer numbers in the following range: [-1000, 1000]

# Efficiency constraints:
# - your function is expected to print the result in less than 2 seconds

# Example:

# Input									Output
# v: 3, -5, 1, -2, 8, -2, 3, -2, 1        15

# Explanation:
# The left sequence is : -5, 1, -2 and the right sequence is: 8, -2, 3.



def maxDifference(v):

	# this function will do the following:
	# find a left subset and a right subset
	# their sums, and the difference between the sums

	# constraints:
	# the difference between these sums needs to be the biggest thing possible
	# (immediately think that we will store something like maxDiff = 0, and then change as iterate through possibilities)
	# the two subsequences should not share any unique elements
	# the two subsequences are at least 2 and at most 1 million numbers
	# all elements in array are from -1000 to 1000 (this is probably a hint...)

	# idea:
	# go through grabbing first subsequence consisting of d (iterate through this value) of the first elements of array
	# go through grabbing second subsequence consisting of the remainer of the elements in the array (ranging from 2 to ...)
	# find sums, calculate differences, store as maximums
	# continue starting from the second elements of array...




# debugging + tracking time
startTime = time.time()
maxDifference([3, -5, 1, -2, 8, -2, 3, -2, 1])
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"

	