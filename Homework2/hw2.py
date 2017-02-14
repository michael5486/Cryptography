from sys import stdout


def XOR(val1, val2):
	if len(val1) != len(val2):
		return -1
	temp = ""
	for i in xrange(0, len(val1)):
		if val1[i] is val2[i]:
			temp += str(0)
		else:
			temp += str(1)	
	
	return temp
	# if val1 is val2:
	# 	return 0
	# else:
	# 	return 1

def expand(A): 
	#line 1
	temp = ""
	temp += str(A[31])
	temp += str(A[0])
	temp += str(A[1])
	temp += str(A[2])
	temp += str(A[3])
	temp += str(A[4])
	
	#line 2
	temp +=  str(A[3])
	temp +=  str(A[4])
	temp +=  str(A[5])
	temp +=  str(A[6])
	temp +=  str(A[7])
	temp +=  str(A[8])

	#line 3
	temp +=  str(A[7])
	temp +=  str(A[8])
	temp +=  str(A[9])
	temp +=  str(A[10])
	temp +=  str(A[11])
	temp +=  str(A[12])
	
	#line 4
	temp +=  str(A[11])
	temp +=  str(A[12])
	temp +=  str(A[13])
	temp +=  str(A[14])
	temp +=  str(A[15])
	temp +=  str(A[16])

	#line 5
	temp +=  str(A[15])
	temp +=  str(A[16])
	temp +=  str(A[17])
	temp +=  str(A[18])
	temp +=  str(A[19])
	temp +=  str(A[20])

	#line 6
	temp +=  str(A[19])
	temp +=  str(A[20])
	temp +=  str(A[21])
	temp +=  str(A[22])
	temp +=  str(A[23])
	temp +=  str(A[24])

	#line 7
	temp +=  str(A[23])
	temp +=  str(A[24])
	temp +=  str(A[25])
	temp +=  str(A[26])
	temp +=  str(A[27])
	temp +=  str(A[28])

	#line 8
	temp +=  str(A[27])
	temp +=  str(A[28])
	temp +=  str(A[29])
	temp +=  str(A[30])
	temp +=  str(A[31])
	temp +=  str(A[0])


	return temp

def printString(string,  numBits):
	
	#numBits = 6

	i = 0
	j = 0
	while i < len(string):
		j = 0
		while j < numBits:
			#stdout.write(string[i + j])
			temp = i + j
			stdout.write(string[i+j])
			j+=1

		stdout.write(" ")
		i += numBits
	stdout.write("\n")	

def doPermutation(string, sBox):
	temp = ""
	for i in range(len(sBox)):
		#grabs value from sbox, adds respective value in string to temp
		temp += str(string[sBox[i] - 1])
	return temp

sBox1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10,0, 6, 13]
sBox2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11,5, 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12 ,6, 9, 3, 2, 15, 13, 8, 10,1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9] 
sBox3 = [1, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12] 
sBox4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

c2d2 = "01010110010110101110101110110101010111010101101101101001"
print "key2", doPermutation(c2d2, pc2)

#101111110000010011110110111100001111011000100010
#0101 0001 1111 1111 0001 1011 0001 1011 1101 1001 1101 1101
#0101 0001 1111 1111 0001 1011 0001 1011 1101 1001 1101 1101


R0 = "00110110010110111101011011001011"
R0expanded = expand(R0)
k1 = "101111110000010011110110111100001111011000100010"
print "R1expanded", R0expanded
print "k1", k1
R0xorK1 = XOR(R0expanded, k1)
print "XOR(R0ex, k1)"
printString(R0xorK1, 6) 
sboxR0 = "11100101101111010001111011011010"
permR0 = doPermutation(sboxR0, p)
#printString(val5, 4)
L0 = "01010110010010111101101110101101"
R1 = XOR(L0, permR0)
print "R1"
printString(R1, 4)

L2 = R1
R1expanded = expand(R1)
k2 = "010100011111111100011011000110111101100111011101"
R1xorK2 = XOR(R1expanded, k2)
print "XOR(R1ex, k2"
printString(R1xorK2, 6)
sboxR1 = "11100100101010100111110011100101"
permR1 = doPermutation(sboxR1, p)
L1 = "00110110010110111101011011001011"
R2 = XOR(L1, permR1)
print "R2"
printString(R2, 4)

L3 = R2
R2expanded = expand(R2)
k3 = "011001011011110111100011000000111101010110110101"
R2xorK3 = XOR(R2expanded, k3)
print "XOR(R2ex, k3)"
printString(R2xorK3, 6)



