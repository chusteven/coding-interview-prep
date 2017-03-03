




import time

# http://www.ardendertat.com/2012/01/06/programming-interview-questions-25-remove-duplicate-characters-in-string/

# note: there is a little too much logic in this thing - also, are we doing the right thing by getting rid of duplicate spaces or what?
# todo: make simpler and also make runtime more efficient



def removeDuplicateCharacters(string):

	# create empty list for characters appeared
	# create empty list for tracking indices of repeated characters
	characters = []
	repeatedCharactersIndices = []

	# iterate through characters in a string
	for i in range(len(string)):
		char = string[i]

		# if character is a space, continue
		if char == " ": continue

		# if character not in characters list, populate list with character
		elif char not in characters: characters.append(char)

		# if character exists in characters list, append index to indices list
		elif char in characters: repeatedCharactersIndices.append(i)

	# print characters
	# print repeatedCharactersIndices

	# delete everything in reverse order (this way don't have to fuck with shifting indices)
	for index in repeatedCharactersIndices[::-1]:
		string = string[:index] + string[index+1:]

	# replace double spaces with single ones
	string = string.replace("  ", " ")

	return string


# example use case
string = "this is a fucking string right here"
string = "tree traversal"



# debugging + tracking time
startTime = time.time()
print removeDuplicateCharacters(string)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"




