
# Check if value in the input is an integer or a word
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
 
# Replace the values in the dictionary with the correctly sorted words/integers       
def go_through(theDict, theList):
	counter = 0
	for k,v in theDict.iteritems():
		theDict[k]   = theList[counter]
		counter      = counter + 1
	return theDict
 
# Replace the values in the original input list with correctly sorted values of the word/int dicts
def inject(theDict, theList):
	for k,v in theDict.iteritems():
		theList[k] = v
	return theList
 

if __name__ == "__main__":
	
	justWords   = {}
	words       = []
	 
	justNums    = {}
	nums        = []

 
	splitInput  = (raw_input("")).split()
 
	# Sort the words and numbers into their own lists as tuples
	for i,j in enumerate(splitInput):
		if is_number(j):
			justNums[i]  = j
			nums.append(j)
		elif not is_number(j):
			justWords[i] = j
			words.append(j)
 
	print("%s\n%s\n" % (justWords, justNums))
 
	words = sorted(words)
	nums  = sorted(nums)
 
	print("%s\n%s\n" % (words, nums))
 
	# Replace the values in the dictionaries with the values in the sorted list
	justWords = go_through(justWords, words)
	justNums  = go_through(justNums, nums)
 
	print("%s\n%s\n" % (justWords, justNums))
 
	# Inject correctly maped sorted words into the original list
	splitInput = inject(justWords, splitInput)
	splitInput = inject(justNums, splitInput)
 
	print("%s" % (' '.join(splitInput)))
 
