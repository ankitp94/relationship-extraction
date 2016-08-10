#            Global Variables
lambdaVal = 0.5

class node(object):
	def __init__(self, Type, Text = ""):
		self.Type = Type.upper()
		self.Text = Text.upper()

def t(R1, R2, i, j):
	if (R1[0])[i].Type == (R2[0])[j].Type and (R1[2])[i] == (R2[2])[j]:
		return 1
	else:
		return 0

def k(R1, R2, i, j):
	if (R1[0])[i].Text == (R2[0])[j].Text:
		return 1
	else:
		return 0

def K(R1, R2, i, j):
	if t(R1, R2, i, j) == 0:
		return 0
	else:
		return k(R1, R2, i, j) + Kc(R1, R2, i, j)

def Kc(R1, R2, i, j):
	L = LArrayCreate(R1, R2, i, j)
	C = CArrayCreate(R1, R2, L, i, j)
	ans = 0
	for ci in range(len(R1[1][i]) + 1):
		for cj in range(len(R2[1][j]) + 1):
			ans += C[ci][cj]
	return ans

def CArrayCreate(R1, R2, L, i, j):
	C = []
	for ci in range(len(R1[1][i]) + 1):
		temp = []
		for cj in range(len(R2[1][j]) + 1):
			temp.append(-1)
		C.append(temp)
	for ci in range(len(R1[1][i]) + 1):
		C[ci][len(R2[1][j])] = 0
	for ci in range(len(R2[1][j]) + 1):
		C[len(R1[1][i])][ci] = 0

	for ci in range(len(R1[1][i])):
		for cj in range(len(R2[1][j])):
			m = len(R1[1][i]) - ci - 1
			n = len(R2[1][j]) - cj - 1
			c1 = R1[1][i][m]
			c2 = R2[1][j][n]
			if t(R1, R2, c1, c2) == 0:
				C[m][n] = 0
			else:
				C[m][n] = C[m+1][n+1]*lambdaVal + (lambdaVal*(1 - (lambdaVal ** L[m][n]))/(1 - lambdaVal))*K(R1, R2, c1, c2)
	return C

def LArrayCreate(R1, R2, i, j):

	## Bhai L kaise compute ho rha hai??
	L = []
	for ci in range(len(R1[1][i]) + 1):
		temp = []
		for cj in range(len(R2[1][j]) + 1):
			temp.append(-1)
		L.append(temp)
	for ci in range(len(R1[1][i]) + 1):
		L[ci][len(R2[1][j])] = 0
	for ci in range(len(R2[1][j]) + 1):
		L[len(R1[1][i])][ci] = 0
	
	# print L

	for ci in range(len(R1[1][i])):
		for cj in range(len(R2[1][j])):
			m = len(R1[1][i]) - ci - 1
			n = len(R2[1][j]) - cj - 1
			c1 = R1[1][i][m]
			c2 = R2[1][j][n]
			if t(R1, R2, c1, c2) == 0:
				L[m][n] = 0
			else:
				L[m][n] = L[m+1][n+1] + 1
	return L

if __name__ == "__main__":
	P17 = node("Entity", "Hardcom Corp.")
	P16 = node("Prep", "of")
	P15 = node("PNP", "scientist")
	P14 = node("PNP", "scientist1")
	P13 = node("Verb", "be")
	P12 = node("Person", "John Smith")
	P11 = node("Sentence", "Complete Sentence")

	P27 = node("Entity", "University")
	P26 = node("Prep", "at")
	P25 = node("PNP", "scientist")
	P24 = node("PNP", "scientist1")
	P23 = node("Verb", "be")
	P22 = node("Person", "James Brown")
	P21 = node("Sentence", "Complete Sentence2")

	R1 = ([P11, P12, P13, P14, P15, P16, P17], [[1,2,3], [], [], [4, 5, 6], [], [], []], ["None", "Member", "None", "None", "None", "None", "Affiliation"])
	R2 = ([P21, P22, P23, P24, P25, P26, P27], [[1,2,3], [], [], [4, 5, 6], [], [], []], ["None", "Member", "None", "None", "None", "None", "Affiliation"])

	print K(R1, R2, 0, 0)
