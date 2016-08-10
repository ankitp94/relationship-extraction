import cPickle
import numpy as np
from sklearn import svm
from KernelSparse1 import *
# from kernel1 import *

def makeKernelMatrix(tuples, lambdaVal):
	temp = [0 for i in range(len(tuples))]
	mat = [[0 for i in range(len(tuples))] for i in range(len(tuples))]
	# for i in range(len(tuples)):
	# 	if(i % 100 == 0):
	# 		print i
	# 	Node = [ tuples[i][0], tuples[i][1], tuples[i][2] ]
	# 	LCA = tuples[i][3]
	# 	mat[i][i] = Kstart(Node, Node, LCA, LCA, lambdaVal)
	for i in range(len(tuples)):
		NODE1 = [ tuples[i][0], tuples[i][1], tuples[i][2] ]
		LCA1 = tuples[i][3]
		if(i % 100 == 0):
			print i
		for j in range(i,len(tuples)):
			# print j
			NODE2 = [ tuples[j][0], tuples[j][1], tuples[j][2] ]
			LCA2 = tuples[j][3]
			mat[i][j] = Kstart(NODE1, NODE2, LCA1, LCA2, lambdaVal)
			mat[j][i] = mat[i][j]
			# print mat[i][j]
	return mat

if __name__ == '__main__':
	tuples = cPickle.load(open("data/sub_1_final_list_of_subexamples.pickle", "rb"))
	tuples += cPickle.load(open("data/sub_2_final_list_of_subexamples.pickle", "rb"))
	tuples += cPickle.load(open("data/sub_3_final_list_of_subexamples.pickle", "rb"))
	y = cPickle.load(open("data/sub_1", "rb"))
	y += cPickle.load(open("data/sub_2", "rb"))
	y += cPickle.load(open("data/sub_3", "rb"))
	for i in range(5, 6):
		print i
		lambdaVal = float(i) * 0.1
		gram = makeKernelMatrix(tuples, lambdaVal)
		fileName = str(lambdaVal) + "changedkmat736.pickle"
		f = open(fileName,'w')
		cPickle.dump(gram, f)
		f.close()

	f = open('y736.pickle','w')
	cPickle.dump(y, f)
	f.close()



