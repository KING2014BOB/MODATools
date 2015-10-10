def multiplicativeInverseCalculator(Z):

	L = []

	for j in range(0,Z):
		arrayCount = 0 


		for i in range(0,Z):
			
			new_item = (i*j) % Z

			print (new_item),

			if new_item == 1 and j > 0:
				L.insert(arrayCount,j)

				arrayCount = arrayCount + 1

		print ("\n")

	return L;

def printList(N):
	for item in N:
		print "Inverse found at %d" % item

#printList(multiplicativeInverseCalculator(5))

printList(multiplicativeInverseCalculator(4))

	
