def palindromecheckr(w,m):
	w1 = list(w.lower())
	w2 = list(m.lower())
	
	#w1.sort()
	#w2.sort()
	pos = 0
	pos2 = 1
	palindrome  = True
	while pos < len(w) and palindrome:
		if w1[pos] == w2[len(w2)-pos2]:
			pos += 1
			pos2 += 1
		else:
			palindrome = False
	return palindrome




print (palindromecheckr('anna','anna'))





