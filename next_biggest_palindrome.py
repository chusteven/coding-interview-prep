




import time

# given a number, find the next smallest palindrome larger than the number
# eg. if the number is 125, next smallest palindrome is 131

# todo: try and do this a more mathematical way (as in use modular arithmetic)
# todo: think, also, about runtime
# http://www.ardendertat.com/2011/12/01/programming-interview-questions-19-find-next-palindrome-number/



def checkPalindrome(number):

	# turn original number into string, also grab reverse of the number
	original = str(number)
	reverse = str(number)[::-1]

	# if they are the same, return True because it is a palindrome; else, return False
	if original == reverse: return True
	else: return False



def checkNextSmallestPalindrome(integer):
	
	# while the integer is not a palindrome, increase the integer by 1
	while not checkPalindrome(integer):
		integer += 1

	# when it is a palindrome, however, then simply return this integer
	return integer



# debugging + tracking time
startTime = time.time()
print checkNextSmallestPalindrome(125)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"





