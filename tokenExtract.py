import re
import sys

# complexity: O(n)
# this method should grow linearly
# using regex, it iterates over each letter – O(n) – in the current line to determine if
# it is alphanumeric; it then uses .lower() – O(n) – to convert it all to lowercase
# and uses extend – O(m), where m represents the number of tokens in the line
# important note is that m will be less than or equal to the number of letters in the line.
def tokenize(FilePath):
	tokenList = []
	with open(FilePath) as infile:
		# goes through each line in the file
		for line in infile:
			# substitute the non-English, non-Alphanumeric characters
			line = re.sub("[^A-Za-z0-9]+", " ", line)
			line = line.lower()
			tokenList.extend(line.split())
	return tokenList


# complexity: O(n)
# iterates over the token list – O(n) – and then it inserts all elements of the token list 
# into a dictionary. The get operation either gets the count of the token or 
# inserts the key and sets its value to 0. Both of these operations are O(1).
def wordFreq(tokenList):
	tokenCount = dict()
	for word in tokenList:
		tokenCount[word] = tokenCount.get(word, 0) + 1
	return tokenCount

# complexity: O(n log n)
# sorting algorithm in Python uses TimSort, which has worst case of O(n log n)
# according to online sources. It then iterates over the elements and prints them – O(n)
def printTokens(tokenDict):	
	sortDict = sorted(tokenDict.items(), key = lambda x: x[1], reverse = True)
	for i, j in sortDict:
		print(i, '=', j)

# main function that just calls the above functions upon running the script
def main():
	# if the correct number of arguments are not provided or 
	# file doesn't exist, handle exception
	try:
		# get the file
		file = sys.argv[1]
		# tokenize and print counts of each token
		tokenList = tokenize(file)
		wordDict = wordFreq(tokenList)
		printTokens(wordDict)
	except:
		pass

if __name__ == '__main__':
	main()

# sources:
# regex101.com – testing the regex above