"""
Implementing binary searching in Python. 
Start at the midpoint in an ordered list,
if the item is the midpoint, then return True
if the item is less than the midpoint, reassign last 
and look in the first half
if the item is greater than the midpoint, reassign last
and look in the last half of the list
"""

def binarySearch(alist,item):
	first = 0
	last = len(alist)-1
	found = False

	while first<=last and not found:
		midpoint = (first+last)//2
		# take care of the base case where the item in question is the middle item
		if alist[midpoint] == item:
			found = True
		else:
			if item<alist[midpoint]:
				last = midpoint+1
			else:
				first = midpoint+1
	return found