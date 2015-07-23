




# todo: think of optimizing things...

import time



def checkBraces(expressions):

    # search for {} or [] or () and get rid of those as we see them
    # then keep on this iteration game until the end
    # we expect the final to be an empty string
    # if not, then we return unbalanced

    for string in expressions:

        # get rid of adjacent matching braces over and over to see what's left over

        # question: how to know when to stop though?
        # answer: when string is empty or when there are no matching thingies

        # while there are no matching brace, get rid of them
        while ("{}" in string) or ("()" in string) or ("[]" in string):

            string = string.replace("{}", "")
            string = string.replace("[]", "")
            string = string.replace("()", "")

        # if the string you end up with is empty, return True (print 1)
        # else, return False (print 0)
        if string == "": print 1
        else: print 0



example = [")(){}", "[]({})", "([])", "{()[]}", "([)]"]



# debugging + tracking time
startTime = time.time()
print checkBraces(example)
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"





