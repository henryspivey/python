# using optional and named arguments
import math
def info(object, spacing=10, collapse=1):
	pass
# spacing and collapse are optional because they have default values.
# Even if info is called with only object passed in, spacing and collapse
# still default to their respective values

# using type,str, dir and other built in functions
print type(1)
li = []
print type(li)
print type(math)

# str coerces anything to a string
print str(1)
horsemen = ['war','pestilence', 'famine']
print horsemen
horsemen.append("powerbuilder")
str(horsemen)
print type(horsemen)

# using dir - prints all the methods for an object
lli = []
print dir(li)
d = {}
print dir(d)
print dir(math)

# using callable - returns a boolean if the object can be called

import string
print string.punctuation
print callable(string.join)


# using getattr
li = ["Larry", "Curly"]
print li.pop
print getattr(li, "pop")
getattr(li, "append")("Moe")
print li

# getattr as a dispatcher
# program that outputs data in various formats with various functions
# use a dispatch function that calls the right one
"""
import statsout
def output(data, format="text"):
	output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
	# third argument is a default value that is returned if the attribute
	# or method specified in the second argument wasn't found
	return output_function(data)
"""

# list filtering
# [mapping expression for element in source-list if filter-expression]
li  = ["a", "mpilgrim", "foo", "b","c","b","d","d"]
print [elem for elem in li if len(elem) >1]
print [elem for elem in li if elem != "b"]
print [li.index(elem) for elem in li if elem =="d"]


