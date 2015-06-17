# Dictionaires - each element is a key value pair
d = {"server":"mpilgrim", "database":"master"}
d['server']
print(d)
d['database'] = "pubs"
print(d)
d['uid'] = "sa"
print(d)

# keys are case sensitive
d = {}
d['key'] = "value"
d["Key"] = "third value"
print d

# you can mix datatypes in a Dictionary
d['henry age']  = 21
print d

# deleting items from a Dictionary
del d['henry age']
print d
d.clear()
print d

# Lists
li = ['a', 'b', 'foo', 'bar']
print li

# lists are zero based and support negative list indices
li[0] # gets the first element
li[-3]

# slicing a list
li[0:3] # doesn't include the element at the end of the range

# adding elements to a list
li.append("new") # adds an element to the end of the list
li.insert(2, "third element")
print li 

li.extend(["two","elements"]) # extend concatenates two lists
# difference between append and extend is how elements are added to the list
# append takes one argument and simply adds it to the end  of the list
# extend takes a single argument, a list, and adds each of the elements of that list
# to the original list

# searching lists 
print li.index("new")
print "new" in li

# deleting list elements
li.remove("new") # removes only the first occurrence

# list operators
# + has the same effect as extend

# tuples - immutable
t = ("a", "b", "c")
print t
# tuples are faster than lists
# tuples "write protect" data that does not change
# tuples can be used as keys in a dictionary
d= {t:"test"}

print d[t]

# assigning multiple values at once to a variable
v = ('a','b','e')
(x,y,z) = v
print x,y,z

# formatting strings
k = "uid"
v = "sa"
print "%s=%s" % (k,v)

userCount = 6
# cannot concatenate 'str' and 'int' objects
# print "Users connected: " + userCount   
# use
print "Users connected: %d" % (userCount,)

# formatting numbers
print "Today's stock price: %f" % 50.4625
print "Today's stock price: %.2f"% 50.4625
print "change since yesterday: %+.2f" %1.5


# mapping lists
li = [1,9,8,4]
print [elem*2 for elem in li]


params = {"server": "mpilgrim", "database":"master",
"uid":"sa", "pwd":"secret"}
print params.keys()
print params.values()
print params.items()
print ["%s=%s" %(i,j) for (i,j) in params.items()]



#joining lists and splitting strings
print ";".join(["%s=%s" %(i,j) for (i,j) in params.items()])
# ; is an object and I am calling its join method
# join method joins the elements of the list into a single string


#splitting a string
li = ["server=mpilgrim", "uid=sa", "database=master", "pwd=secret"]
s = ";".join(li)
print s
print s.split(";")
