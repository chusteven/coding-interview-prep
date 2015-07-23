




import time

# find the first non-repeated (unique) character in a given string



def firstUniqueCharacter(string):

	# create empty dictionary to be populated with counts of characters in string
	dictionary = {}

	# iterate through characters and populate dictionary with counts
	for char in string:
		if char not in dictionary: dictionary[char] = 1
		else: dictionary[char] += 1

	# grabbing all unique characters (counts are 1)
	# for key, value in dictionary.iteritems():
	# 	if value == 1: print key

	# iterating through characters in string
	for char in string:

		# if that character is one of the unique ones
		# print the character and break the loop
		if dictionary[char] == 1:
			print char
			break

		# otherwise, continue in the loop
		else:
			continue



# example use case
string = "this is a sentence and i think the answer to this would be..."
# uniqueCharacters = ["c", "b", "k", "l", "r", "u"]



# debugging
startTime = time.time()
firstUniqueCharacter(string)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"






