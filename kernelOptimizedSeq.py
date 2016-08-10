#            Global Variables
lambdaVal = 0.5

class node(object):
	def __init__(self, Type, Role = "none", Text = ""):
		self.Type = Type.upper()
		self.Role = Role.upper()
		self.Text = Text.upper()

class relation(object):
	def __init__(self, first, child, isRoot = False):
		self.first = first
		self.child = child
		self.isRoot = isRoot
		self.parent = None

	def insertChild(self, child):
		self.child = (self.child).append(child)

	def size(self):
		return len(self.child)

	def setMyParent(self, parent):
		self.parent = parent

	def setChildParent(self):
		for it in range(len(self.child)):
			(self.child)[it].setMyParent(self)

def t(R1, R2):
	if (R1.first).Type == (R2.first).Type and (R1.first).Role == (R2.first).Role:
		return 1
	else:
		return 0

def k(R1, R2):
	if (R1.first).Text == (R2.first).Text:
		return 1
	else:
		return 0

def K(R1, R2):
	if t(R1, R2) == 0:
		return 0
	else:
		return k(R1, R2) + Kc(R1, R2)

def Kc(R1, R2):
	L = LArrayCreate(R1, R2)
	C = CArrayCreate(R1, R2, L)
	ans = 0
	for i in range(R1.size() + 1):
		for j in range(R2.size() + 1):
			ans += C[i][j]
	return ans

def CArrayCreate(R1, R2, L):
	C = []
	for i in range(R1.size() + 1):
		temp = []
		for j in range(R2.size() + 1):
			temp.append(-1)
		C.append(temp)
	for i in range(R1.size() + 1):
		C[i][R2.size()] = 0
	for i in range(R2.size() + 1):
		C[R1.size()][i] = 0

	for i1 in range(R1.size()):
		for j1 in range(R2.size()):
			i = R1.size() - i1 - 1
			j = R2.size() - j1 - 1
			if t(R1.child[i], R2.child[j]) == 0:
				C[i][j] = 0
			else:
				C[i][j] = C[i+1][j+1]*lambdaVal + (lambdaVal*(1 - (lambdaVal ** L[i][j]))/(1 - lambdaVal))*K(R1.child[i], R2.child[j])
	return C

def LArrayCreate(R1, R2):

	## Bhai L kaise compute ho rha hai??
	L = []
	for i in range(R1.size() + 1):
		temp = []
		for j in range(R2.size() + 1):
			temp.append(-1)
		L.append(temp)
	for i in range(R1.size() + 1):
		L[i][R2.size()] = 0
	for i in range(R2.size() + 1):
		L[R1.size()][i] = 0
	
	# print L

	for i in range(R1.size()):
		for j in range(R2.size()):
			if t(R1.child[R1.size() - i - 1], R2.child[R2.size() - j - 1]) == 0:
				L[R1.size() - i - 1][R2.size() - j - 1] = 0
			else:
				L[R1.size() - i - 1][R2.size() - j - 1] = L[R1.size() - i][R2.size() - j] + 1
	return L




if __name__ == "__main__":
	P17 = node("Entity", "Affiliation", "Hardcom Corp.")
	P16 = node("Prep", "none", "of")
	P15 = node("PNP", "none", "scientist")
	P14 = node("PNP", "none", "scientist1")
	P13 = node("Verb", "none", "be")
	P12 = node("Person", "Member", "John Smith")
	P11 = node("Sentence", "None", "Complete Sentence")

	P27 = node("Entity", "Affiliation", "University")
	P26 = node("Prep", "none", "at")
	P25 = node("PNP", "none", "scientist")
	P24 = node("PNP", "none", "scientist1")
	P23 = node("Verb", "none", "be")
	P22 = node("Person", "Member", "James Brown")
	P21 = node("Sentence", "None", "Complete Sentence2")

	R17 = relation(P17, [])
	R16 = relation(P16, [])
	R15 = relation(P15, [])
	R14 = relation(P14, [R15, R16, R17])
	R14.setChildParent()
	R13 = relation(P13, [])
	R12 = relation(P12, [])
	R11 = relation(P11, [R12, R13, R14], True)
	R11.setChildParent()

	R27 = relation(P27, [])
	R26 = relation(P26, [])
	R25 = relation(P25, [])
	R24 = relation(P24, [R25, R26, R27])
	R24.setChildParent()
	R23 = relation(P23, [])
	R22 = relation(P22, [])
	R21 = relation(P21, [R22, R23, R24], True)
	R11.setChildParent()

	print K(R11, R21)
