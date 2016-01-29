import BasicPrime

#Power computations
n = 7

def primeFunctionChoice(n):

	if(n==1):
		return isItPrime()

	else:
		return BasicPrime.isItProbablyPrime()


def isItPrime(number,exponent):
	lucasLehmerList = []
	result = False

	possiblePrime = (number ** exponent) - 1
	print possiblePrime

	lucasLehmerList = generateLucasLehmerNumbers(n)

	if (lucasLehmerList[exponent-2] % possiblePrime == 0):
		result = True

	else:
		result = False

	return result

def primeCalculator(noNums):

	primeList = []

	for i in range(1,noNums + 1):
		probablePrime = isItProbablyPrime(i)
		#print("is %d prime: %s" % (i,isItProbablyPrime(i)) )

		if probablePrime == True:
			primeList.append(i)

	print(primeList)
	return probablePrime


def generateLucasLehmerNumbers(noNums):

	lucasLehmerList = []
	for i in range(1,n + 1):
		lucasLehmerList.append(getLucasLehmerNumber(i))

	return(lucasLehmerList)


def getLucasLehmerNumber(N):

	if( N <= 1 ):
		return 4

	else:
		return ((getLucasLehmerNumber(N-1) ** 2) - 2)

isItPrime(2,3)
#primeCalculator(30)

print(BasicPrime.isItProbablyPrime(7))

