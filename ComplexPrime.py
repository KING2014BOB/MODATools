import TestSuite

n = 100

def getLucasLehmerNumber(N):

	if( N <= 1 ):
		return 4

	else:
		return ((getLucasLehmerNumber(N-1) ** 2) - 2)

def isItPrime(number,exponent):
	lucasLehmerList = []
	result = False

	possiblePrime = (number ** exponent) - 1

	#TestSuite.printTesting(possiblePrime)

	lucasLehmerList = generateLucasLehmerNumbers(n,possiblePrime)

	if (lucasLehmerList[exponent-2] % possiblePrime == 0):
		result = True

	else:
		result = False

	return result

def generateLucasLehmerNumbers(noNums,possiblePrime):

	lucasLehmerList = []
	for i in range(1,n + 1):

		newNumber = getLucasLehmerNumber(i)

		if newNumber > possiblePrime:
			lucasLehmerList.append(newNumber % possiblePrime )

		else:
			lucasLehmerList.append(newNumber)

	return(lucasLehmerList)