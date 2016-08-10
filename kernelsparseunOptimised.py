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
	ans = 0
	# for i in range(R1.size()):
	# 	for j in range(R2.size()):
	# 		for length in range(R1.size()):
	# 			if(i + length < R1.size() and j + length < R2.size()):
	# 				prod = 1
	# 				for it in range(length + 1):
	# 					prod = prod * t(R1.child[i + it], R2.child[j + it])
	# 					# if i + length < R1.size() and j + length < R2.size():
	# 				for it in range(length + 1):
	# 					# print "calling function K with ", (R1.child[i + it]).first.Text, (R2.child[j + it]).first.Text
	# 					ans += (lambdaVal**(length + 1)) * prod * K(R1.child[i + (it)], R2.child[j + (it)])

	# for length in range(R1.size()):
	# 	# print "length = ", length
	# 	for i in range(R1.size()):
	# 		for j in range(R2.size()):
	# 			if(i + length < R1.size() and j + length < R2.size()):
	# 				prod = 1
	# 				for it in range(length + 1):
	# 					prod = prod * t(R1.child[i + it], R2.child[j + it])
	# 				for it in range(length + 1):
	# 					# print "calling function K with ", (R1.child[i + it]).first.Text, (R2.child[j + it]).first.Text
	# 					ans += (lambdaVal**(length + 1)) * prod * K(R1.child[i + (it)], R2.child[j + (it)])
	# 	# print ans

	
	return ans

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
