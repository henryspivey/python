import random
def generateOne(strlen):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	res = ""
	for i in range(strlen):
		res = res + alphabet[random.randrange(27)]

	return res


def score(goal,teststring):
	numSame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numSame +=1
	return float(numSame)/float(len(goal))

def main():
	goalString = "water" # feel free to change this line
	newString = generateOne(5) # change the number here depending on how long the word is
	best = 0
	count  = 0
	newScore = score(goalString,newString)
	while  newScore < 1:
		if newScore > best:
			
			print ('%'+str(newScore)+ " accurate",newString)
			best = newScore

		newString = generateOne(5)  # change the number here depending on how long the word is
		newScore = score(goalString,newString)
		
		count  = count + 1
		if newScore == 1:
			print ("You entered: " + newString)
main()



