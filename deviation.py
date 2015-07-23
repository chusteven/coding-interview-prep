




import time

# todo: think about runtime - perhaps ways to optimize runtime for for loop, list comprehension, checking whether maximum



def findDeviation(v, d):

    # these are all the indices i will have to check
    iterations = len(v) - d

    # define current maximum
    maxDeviation = 0
    
    # iterate through the indices i need to check
    for i in range(iterations):

        # grab the d elements i need to
    	elements = [v[i+j] for j in range(d)]
        
        # calculate deviation between maximum and minimum of elements
        deviation = max(elements) - min(elements)
        
        # if this is greater than the current maximum deviation, then replace as this value
        if deviation > maxDeviation: maxDeviation = deviation
    
    # print out final maximum deviation
    print maxDeviation



# example use case
values = [9, 4, 7, 1, 2, 3, 10, 4, 5, 9, 12, 15, 20]
distance = 3



# debugging + tracking time
startTime = time.time()
findDeviation(values, distance)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"





