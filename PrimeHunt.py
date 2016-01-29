def hunt(noNums):
	return 

def primeCalculator(noNums):

	for i in range(1,noNums + 1):
		print("is %d prime: %s" % (i,isItProbablyPrime(i)) )

def isItProbablyPrime(possiblePrime):
	lucasNumbersArray = []

	result = False
	lucasNumbersArray = generateLucasNumbers(20)

	comparisonNo = lucasNumbersArray[possiblePrime-1]

	#print((comparisonNo - 1) % possiblePrime )

	if (comparisonNo - 1) % possiblePrime == 0:
		result = True

	else:
		result = False

	return result

def generateLucasNumbers(noNums):
	list = []

	for i in range(0,noNums +  1):
		list.append(lucasNumber(i))

	return list

def lucasNumber(N):
    if( N == 0 ):
    	return 1

    elif( N == 1 ):
    	return 3

    else:
    	return lucasNumber(N-1) + lucasNumber(N-2);

primeCalculator(20)

