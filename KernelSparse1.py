#            Global Variables
# lambdaVal = 0.5

class node(object):
	def __init__(self, Type, Text = ""):
		self.Type = Type.upper()
		self.Text = Text.upper()
		self.Orig = None
		self.Parent = None

def t(R1, R2, i, j):
	if (R1[0])[i].Type == (R2[0])[j].Type and (R1[2])[i] == (R2[2])[j]:
		return 1
	else:
		return 0

def k(R1, R2, i, j):
	# print "Hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
	# if (R1[2])[i] == (R2[2])[j] and (R1[2])[i] in ["ORG", "MEMBER"]:
	# 	return 1000
	if (R1[0])[i].Text == (R2[0])[j].Text:
		return 1000
	else:
		return 0

def Kstart(R1, R2, i, j, lambdaVal):
	# lambdaVal = val
	# print lambdaVal
	if t(R1, R2, i, j) == 0:
		return 0
	else:
		return k(R1, R2, i, j) + Kc(R1, R2, i, j, lambdaVal)

def K(R1, R2, i, j, lambdaVal):
	if t(R1, R2, i, j) == 0:
		return 0
	else:
		return k(R1, R2, i, j) + Kc(R1, R2, i, j, lambdaVal)

def Kc(R1, R2, i, j, lambdaVal):
	ans = 0
	for it in range(min(len(R1[1][i]), len(R2[1][j]))):
		ans += Kcq(R1, R2, i, j, len(R1[1][i]) - 1, len(R2[1][j]) - 1, it, lambdaVal)
	return ans

def Kcq(R1, R2, x, y, i, j, q, lambdaVal):
	if(i < 0 or j < 0):
		return 0
	if(q > min(i, j)):
		return 0
	ans = lambdaVal * Kcq(R1, R2, x, y, i, j-1, q, lambdaVal)
	for s in range(i):
		ans += t(R1, R2, R1[1][x][s], R2[1][y][j]) * lambdaVal * lambdaVal * CqWitha(R1, R2, x, y, s -1, j - 1, K(R1, R2, R1[1][x][s], R2[1][y][j], lambdaVal), q-1, lambdaVal)
	return ans

def CqWitha(R1, R2, x, y, i, j, a, q, lambdaVal):
	if(i < 0 or j < 0):
		return 0
	if(q > min(i, j)):
		return 0
	if(q == 0):
		return 1
	ans = 0
	ans += a * CqWithOuta(R1, R2, x, y, i, j, q, lambdaVal)
	for r in range(q):
		ans += Cqr(R1, R2, x, y, i, j, q, r, lambdaVal)
	return ans

def CqWithOuta(R1, R2, x, y, i, j, q, lambdaVal):
	if(i < 0 or j < 0):
		return 0
	if(q > min(i, j)):
		return 0
	if(q == 0):
		return 1
	ans = 0
	ans += lambdaVal * CqWithOuta(R1, R2, x, y, i , j - 1, q, lambdaVal) + CqPrime(R1, R2, x, y, i, j, q, lambdaVal)
	return ans

def CqPrime(R1, R2, x, y, i, j, q, lambdaVal):
	if(i < 0 or j < 0):
		return 0
	if(q > min(i, j)):
		return 0
	return t(R1, R2, R1[1][x][i], R2[1][y][j]) * lambdaVal * lambdaVal * CqWithOuta(R1, R2, x, y, i - 1, j - 1, q - 1, lambdaVal) + lambdaVal * CqPrime(R1, R2, x, y, i, j - 1, q, lambdaVal)

def Cqr(R1, R2, x, y, i, j, q, r, lambdaVal):
	if(i < 0 or j < 0):
		return 0
	if(q > min(i, j) or q < r):
		return 0
	ans = 0
	ans += lambdaVal * Cqr(R1, R2, x, y, i, j - 1, q, r, lambdaVal) + CqrPrime(R1, R2, x, y, i, j, q, r, lambdaVal)
	return ans

def CqrPrime(R1, R2, x, y, i, j, q, r, lambdaVal):
	if(i < 0 or j < 0):
		return 0
	if(q > min(i, j) or q < r):
		return 0
	if q != r :
		ans = t(R1, R2, R1[1][x][i], R2[1][y][j])
		return ans * lambdaVal * lambdaVal * Cqr(R1, R2, x, y, i - 1, j - 1, q - 1, r, lambdaVal) + lambdaVal * CqrPrime(R1, R2, x, y, i, j - 1, q, r, lambdaVal)
	else :
		return t(R1, R2, R1[1][x][i], R2[1][y][j]) * lambdaVal * lambdaVal * K(R1, R2, R1[1][x][i], R2[1][y][j], lambdaVal) * CqWithOuta(R1, R2, x, y, i - 1, j - 1, q - 1, lambdaVal) + lambdaVal * CqrPrime(R1, R2, x, y, i, j - 1, q, r, lambdaVal)

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

	R1 = ([P11, P12, P13, P14, P15, P16, P17], [[1,2,3], [], [], [4, 5, 6], [], [], []], ["None", "MEMBER", "None", "None", "None", "None", "ORG"])
	R2 = ([P21, P22, P23, P24, P25, P26, P27], [[1,2,3], [], [], [4, 5, 6], [], [], []], ["None", "MEMBER", "None", "None", "None", "None", "ORG"])

	print K(R1, R2, 0, 0, 0.5)
