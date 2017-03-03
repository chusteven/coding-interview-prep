




import time

# given an integer array, output all pairs that sum up to a specific value k
# note: http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/



def arrayPairSum(v, k):

	# note: this is O(n^2) because we are iterating through each element (n) and checking whether k-element is also in the array (n)

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



def pairSum1(arr, k):

	# note this is O(n*log(n)) because ...

	# if the array is of length 1 or 0, then simply return the function
    if len(arr)<2: return

    # sort the array
    arr.sort()

    # create pointers from the left- and right-hand end points
    left, right = (0, len(arr)-1)

    # while the two points have not met
    while left < right:

    	# calculate current sum of the two things...
        currentSum = arr[left] + arr[right]

        # if the current sum equals k, then print these two values of the array
        # also increase the left hand pointer so that we eventually move beyond the right-hand pointer and the loop stops
        if currentSum == k: 
        	print arr[left], arr[right]
        	left += 1 # or right-=1

        # if the current sum is less than k, then increase the left-hand pointer (to make the sum bigger)
        elif currentSum < k:
            left += 1

        # in the case the current sum is greater than k, then decrease the right-hand pointer (to make the sum smaller)
        else:
            right -= 1



def pairSum2(arr, k):

	# note: this is O(n) because ...

	# if the array is of length 1 or 0, then simply return the function
    if len(arr) < 2:
        return

    # create sets for seen (elements) and outputs (pairs we want to keep track of)
    seen = set()
    output = set()

    # iterate through numbers in array
    for num in arr:

    	# calculate target value (complimentary pari)
        target = k - num

        # if the target has not been seen
        if target not in seen:

        	# add this number to the seen set
            seen.add(num)

        # otherwise, we know that we have found a pair for what number we're looking at currently and what we've already seen
        else:

        	# add to output set as tuple (x, y)
            output.add( (min(num, target), max(num, target)) )

    # print all these outputs
    print '\n'.join( map(str, list(output)) )



# example use case
values = [1, 4, 5, 0, 10, -5, 2, 3, 1, 6, 7, 8, 9, 12, 15, -2, -3, 1, 4]
sumValue = 5

# debugging
pairSum2(values, sumValue)