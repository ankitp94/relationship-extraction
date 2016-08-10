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
	# if (R1[2])[i] == (R2[2])[j] and (R1[2])[i] in ["ORG", "MEMBER"]:
	# 	# print "Hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
	# 	return 1
	if (R1[0])[i].Text == (R2[0])[j].Text:
		return 1
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
	for length in range(len(R1[1][i])):
		for ci in range(len(R1[1][i])):
			for cj in range(len(R2[1][j])):
				if(ci + length < len(R1[1][i]) and cj + length < len(R2[1][j])):
					prod = 1
					for it in range(length + 1):
						prod = prod * t(R1, R2, R1[1][i][ci + it], R2[1][j][cj + it])
					for it in range(length + 1):
						ans += (lambdaVal**(length + 1)) * prod * K(R1, R2, R1[1][i][ci + it], R2[1][j][cj + it], lambdaVal)
	return ans

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
