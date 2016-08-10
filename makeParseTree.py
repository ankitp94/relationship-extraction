import KernelSparse
import sys
sys.path.insert(0, '/home/asus/Downloads/parser/corenlp-python')
from corenlp import StanfordCoreNLP
class node(object):
	def __init__(self, Type, Text = ""):
		self.Type = Type.upper()
		self.Text = Text.upper()
		self.Orig = None
		self.Parent = None

# CORENLP_dir = "/home/asus/Downloads/parser/corenlp-python/stanford-corenlp-full-2015-04-20"
# CORENLP = StanfordCoreNLP(CORENLP_dir)  # wait a few minutes...
# 	# return CORENLP

import make_tree
import cPickle

def getParsedOutput(sentence,CORENLP):
	result = CORENLP.raw_parse(sentence)
	return result

def traverseTree(node_list,adjacency,word_lemma_role):
	role_list = [None for j in range(len(node_list))]
	# print word_lemma_role.keys()
	# for i in range(2):
	# 	node_list[i].Text=""
	for i in range(len(node_list) - 2):
		j = i +2 
		cur_node = node_list[j]
		cur_node.Text = cur_node.Text.strip()
		cur_adjacency = adjacency[j]
		# print "a   ",  cur_node.Text , len(cur_node.Text) 
		if cur_node.Text in word_lemma_role.keys():
			# print "here"
			cur_node.Orig = cur_node.Text
			cur_node.Text = word_lemma_role[cur_node.Text][0]
			role_list[j] = word_lemma_role[cur_node.Orig][1]
	for i in range(len(node_list)-2):
		j = len(node_list) - 1 - i
		cur_node = node_list[j]
		cur_adjacency = adjacency[j]
		if len(cur_adjacency) != 0:
			if cur_node.Type == "NP":
				initialText = node_list[cur_adjacency[0]].Text
				for j in cur_adjacency:
					cur_child = node_list[j]
					if cur_child.Type in ["NP","NNP","NNS","NNPS","NN"]:
						initialText = cur_child.Text
						break
				cur_node.Text = initialText
			elif cur_node.Type == "VP":
				initialText = node_list[cur_adjacency[0]].Text
				for j in cur_adjacency:
					cur_child = node_list[j]
					if cur_child.Type in ["VP","VB","VBD","VBG","VBN","VBP","VBZ",] :
						initialText = cur_child.Text
						break
				cur_node.Text = initialText
			else :
				initialText = node_list[cur_adjacency[0]].Text
				cur_node.Text = initialText
				# To DO
				# Can change the text to the first child

	return node_list,adjacency,role_list


def makeTree(result):
	parsedInput = result['sentences'][0]['parsetree']
	# print result
	items = parsedInput.split(']')
	newItem = []
	newItem.append(items[len(items) - 1])
	node,adjacency = make_tree.mk_tree(newItem[0])
	items.pop()
	word_lemma_role = {}
	organisation = []
	for it in range(len(items)):
		words = items[it].split()
		temp = []
		for i in words:
			temp.append((i.split('='))[1])
		cur_word = temp[0]
		cur_role = None
		if(temp[5] == "ORGANIZATION"):
			cur_role = "ORG"
		if(temp[5] == "PERSON"):
			cur_role = "PERSON"
		cur_lemma = temp[4]
		word_lemma_role[cur_word.upper().encode('utf-8')] = (cur_lemma.upper().encode('utf-8'),cur_role)
		newItem.append(temp)
	# role_list = []
	# print word_lemma_role
	node, adjacency, role = traverseTree(node,adjacency,word_lemma_role)
	return node, adjacency, role

def setAllParents(node_list, adjacency_list):
	for k in range(len(adjacency_list)):
		for i in adjacency_list[k]:
			node_list[i].Parent = k
	return node_list, adjacency_list

def joinOrgNodes(node_list, adjacency_list, new_role_list):
	join_nodes = []
	deletedNodes = []
	finalIndex = [0 for i in range(len(node_list))]
	count = 0
	for i in range(len(node_list) + 1):
		if(i == len(node_list)):
			if(count > 0):
				join_nodes.append((i - count,count))
			count = 0
		elif(new_role_list[i] == "ORG"):
			if(count != 0):
				deletedNodes.append(i)
			count+=1;
		else:
			if(count > 0):
				join_nodes.append((i - count,count))
			count = 0
	join_nodes.reverse()
	dec = 0

	j = 0
	for i in range(len(finalIndex)):
		if j < len(deletedNodes):
			if i >= deletedNodes[j]:
				dec += 1
				j = j + 1
			finalIndex[i] = i - dec

	for start, count in join_nodes:
		new_text = ""
		new_adjacency = []
		for i in range(count):
			if new_text == "":
				new_text = node_list[start + i].Text
			else:
				new_text = new_text + " " + (node_list[start + i].Text) 
			new_adjacency = new_adjacency + adjacency_list[start + i]
		node_list[start].Text = new_text
		adjacency_list[start] = new_adjacency
	# for i in range(len(node_list)):
	# 	print node_list[finalIndex[i]].Parent, node_list[finalIndex[i]].Text
	for i in range(1, len(finalIndex)):
		if(finalIndex[i] == finalIndex[i-1]):
			node_list.remove(node_list[finalIndex[i] + 1])
			adjacency_list.remove(adjacency_list[finalIndex[i] + 1])
			new_role_list.remove(new_role_list[finalIndex[i] + 1])
	final_adjacency = []
	for i in range(len(adjacency_list)):
		newList = []
		for k in adjacency_list[i]:
			if(k != 0):
				if(finalIndex[k] != finalIndex[k - 1]):
					newList = newList + [finalIndex[k]]
		final_adjacency.append(newList)
	return node_list, adjacency_list, new_role_list

def getAncestors(node_list, it):
	ancestors = []
	ancestors = ancestors + [it]
	while(node_list[it].Parent != None):
		ancestors = ancestors + [node_list[it].Parent]
		it = node_list[it].Parent
	ancestors.reverse()
	return ancestors

def assignRoles(node_list, adjacency_list, role_list):
	NP_list = []
	org_list = []
	sol = []
	# node_list, adjacency_list, role_list = joinOrgNodes(node_list, adjacency_list, role_list)
	node_list, adjacency_list = setAllParents(node_list, adjacency_list)
	for i in range(len(node_list)):
		if node_list[i].Type in ["NP","NNS","NN"] and role_list[i] != "ORG":
			NP_list.append(i)
		if node_list[i].Type in ["NP","NNP","NNS","NNPS","NN"] and role_list[i] == "ORG":# check coorporation
			if len(org_list) > 0 and ((org_list[-1] == (i -1)) or  role_list[i-1] == "ORG" ):
				pass
			else:
				org_list.append(i)
	for org in org_list:
		orgAncestors = getAncestors(node_list, org)
		for NP in NP_list:
			new_role_list = [None for i in range(len(role_list))]
			new_role_list[org] = "ORG"
			flag = 1
			for child in (adjacency_list[NP]):
				if(role_list[child] == "ORG"):
					flag = 0
			if flag == 1:
				new_role_list[NP] = "MEMBER"
				memberAncestors = getAncestors(node_list, NP)
				numCommonAncestors = 0
				while(numCommonAncestors < len(memberAncestors) and numCommonAncestors < len(orgAncestors) and memberAncestors[numCommonAncestors] == orgAncestors[numCommonAncestors]):
					numCommonAncestors = numCommonAncestors + 1
				numCommonAncestors = numCommonAncestors - 1
				lastCommonAncestor = memberAncestors[numCommonAncestors]
				sol.append((node_list, adjacency_list, new_role_list, lastCommonAncestor))
	return sol

# CORENLP1 = startCoreNLP()
# sent = "John Smith is a scientist at Harvard ."
# print makeTree(getParsedOutput(sent))

---------------------------------------
if __name__ == "__main__":

	tuple = cPickle.load(open("tuple_of_node_adjacency_role", "rb"))
	node = tuple[0]
	adjacency = tuple[1]
	role = tuple[2]
	for i in range(len(node)):
		print i, node[i].Text, node[i].Parent, adjacency[i], role[i], node[i].Type
	sol = assignRoles(node, adjacency, role)
	print len(sol)
	for i in sol:
		print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
		for k in range(len(i[0])):
			print k, "\tparent", sol[0][0][k].Parent, "\tadjacency", sol[0][1][k], "\tRole", sol[0][2][k], sol[0][3], sol[0][0][k].Text

