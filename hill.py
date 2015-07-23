




# this is the function written in javascript
# https://gist.github.com/liyu1981/8731977

function hill(v) {
    for (var i = 0; i < 10; i++) {
        var current = v[0] - i;
        for (var k = 1; k < v.length; k++) {
            current++;
            if (v[k] >= current) {
                if (v[k] - current > i) {
                    current = v[k] - i;
                }
            } else {
                if (current - v[k] > i) break;
            }
        }
        if (k === v.length) {
            console.log(i)
            return i;
        }
    }
}



# this is my function...

def hill(v):
    # goal is to obtain a strictly sorted, ascending list
    # this means we want the first element to be the smallest
    # we want the last element to the be biggest
    # and everything in between to fall as necessary
    
    # store nothing in here originally
    state = {"off": None, "max": None}

    # go through each element of the inputted list
    for i in range(len(v)):

    	# if it is the first element,
    	# set max to that value
    	# set offset to 0
        if i == 0:
            state["off"] = 0
            state["max"] = v[i]

        # if not the first element, have to run some comparisons
        else:

        	# if this element is bigger than the max, then store the max as this new element
            if v[i] > state["max"]:
                state["max"] = v[i]

            # otherwise, have to run some more comparisons
            else:

            	# create variable o to be equal to the current maximum minus this element
            	# note: this helps us determine how big things need to be offset
                o = state["max"] - v[i]

                if o > state["off"]:
                    state["off"] = o

                elif o == state["off"]:
                    state["off"] = state["off"] + 1

                # else:
                #     continue
                #     # state["off"] = state["off"]

        state["max"] = state["max"]

    print state["off"]



# example use cases/debugging
hill([5, 4, 3, 2, 8])
hill([5, 4, 3, 4, 8])
hill([5, 4, 3, 0, 8])
hill([3, 3, 2])



# debugging + tracking time
startTime = time.time()
hill([5, 4, 3, 0, 8])
print "\n", ("--- total runtime: %s seconds ---" % (time.time() - startTime)), "\n"




