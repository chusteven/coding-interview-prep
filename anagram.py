




import time

# todo: think about runtime - are there better ways to check whether something is in dictionary or not?



def anagram(firstWords, secondWords):
    
    # iterate through the length of the two lists
    for i in range(len(firstWords)):
        
        # initialize empty dictionaries for counting characters in each word
        wordOne = {}
        wordTwo = {}

        # iterate through characters in first word, check to see if in dictionary (if so, add 1 to current value; else, store 1 as value)
        for char in firstWords[i]:
            if char in wordOne: wordOne[char] += 1
            else: wordOne[char] = 1

        # same for second word
        for char in secondWords[i]:
            if char in wordTwo: wordTwo[char] += 1
            else: wordTwo[char] = 1

        # if the counts for each thing match, then print 1; else 0
        if wordOne == wordTwo: print 1
        else: print 0



# example use cases
wordsOne = ['banana', 'word', 'dad', 'torrie', 'momma']
wordsTwo = ['annaba', 'drow', 'add', 'torrys', 'mmmai']



# debugging + tracking time
startTime = time.time()
anagram(wordsOne, wordsTwo)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"



