




import time

# given an integer array, output all pairs that sum up to a specific value k
# note: http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/

# todo: i've not O(n^2), want O(nlog(n)), can also get down to O(n) with appropriate algorithm



def arrayPairSum(v, k):

	# go through each element (x) in list
	# try and find whether complement (y) exists
	# if it does, print that tuple (x, y)
	# else, continue on the iteration

	for i in range(len(v)):
		x = v[i]
		y = k - x

		remainder = v[:i] + v[i+1:]

		if y in remainder: print (x, y)
		else: continue



# example use case
values = [1, 4, 5, 0, 10, -5, 2, 3, 1, 6, 7, 8, 9, 12, 15, -2, -3, 1, 4]
sumValue = 5



# debugging + tracking time
startTime = time.time()
arrayPairSum(values, sumValue)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"



