




import time

# given a number, find the next higher number using only the digits in the given number
# for example if the given number is 1234, next higher number with same digits is 1243



def findNextHighestSameDigits(number):

	# converting number to string (for easy access of digits as characters in string)
	stringNumber = str(number)

	# create empty dictionary to be populated with characters and counts
	dictOriginalNumber = {}

	# populate dictionary with counts of digits
	for num in stringNumber:
		if num not in dictOriginalNumber: dictOriginalNumber[num] = 1
		else: dictOriginalNumber[num] += 1

	# defining new numbers' dictionary
	dictNewNumber = {}

	# while the new number doesn't have the same digits
	while dictOriginalNumber != dictNewNumber:

		# increase the number, create new dictionary to be populated with new digits
		number += 1
		stringNumber = str(number)
		dictNewNumber = {}

		for num in stringNumber:
			if num not in dictNewNumber: dictNewNumber[num] = 1
			else: dictNewNumber[num] += 1

	# when the while loop breaks (and it will), print this number
	print number



# example use cases
num = 1234
num = 1254
num = 1122
num = 1561



# debugging
startTime = time.time()
findNextHighestSameDigits(num)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"




