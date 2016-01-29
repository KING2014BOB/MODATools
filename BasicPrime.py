import TestSuite

#Smaller computations
N = 10

def generateLucasNumbers(noNums):
	list = []

	for i in range(0,noNums +  1):
		list.append(getLucasNumber(i))

	return list

def getLucasNumber(N):
    if( N == 0 ):
    	return 1

    elif( N == 1 ):
    	return 3

    else:
    	return getLucasNumber(N-1) + getLucasNumber(N-2);

def isItProbablyPrime(possiblePrime):

	global N

	lucasNumbersArray = []

	result = False
	lucasNumbersArray = generateLucasNumbers(N)

	comparisonNo = lucasNumbersArray[possiblePrime-1]

	#print((comparisonNo - 1) % possiblePrime )

	if (comparisonNo - 1) % possiblePrime == 0:
		result = True

	else:
		result = False

	return result