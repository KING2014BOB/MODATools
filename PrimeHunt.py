import BasicPrime
import ComplexPrime
import TestSuite

mode = 0

def setup():

	global mode

	print("Do you want to use")
	print("1: Basic")
	print("2: Complex")
	

	choice = raw_input("Do you want to use 1:Basic or 2:Complex:")
	choice = int(choice)

	if(choice == 1):
		mode = 1

	elif(choice == 2):
		mode = 2

	else:
		print("incorrect choice")


def primeFunctionChoice(number,exponent):

	if(mode==2):
		return ComplexPrime.isItPrime(number,exponent)

	else:
		return BasicPrime.isItProbablyPrime(number)


def primeCalculator(noNums):

	primeList = []
	primeValues = []
	probablePrimeBool = False

	if mode == 1:
		j = 1

	else:
		j = 2


	for i in range(j,noNums):
		probablePrimeBool = primeFunctionChoice(2,i)

		if probablePrimeBool == True:
			primeList.append("2^%d-1" % i)

	return primeList


setup()

print(primeCalculator(100))

#print(BasicPrime.isItProbablyPrime(7))
#print(ComplexPrime.isItPrime(2,3))

#print(ComplexPrime.isItPrime(3,4))

