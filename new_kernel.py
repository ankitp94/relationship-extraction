from kernel1 import *
import cPickle
def compute_if_preterminal_node(tree,i):
	children=tree[1][i]
	result=1
	for child in children:
		if(len(tree[1][child])>0):
			result=0
	return result
def compute_kernel(tree1,tree2,delta):
	tree_match_val=[[0]*len(tree2[0])]*len(tree1[0])
	root1=tree1[3]
	root2=tree2[3]
	#tree2_val=[0]*len(tree2[0])
	for i in range(0,len(tree1[0])-root1):
		for j in range(0,len(tree2[0])-root2):
			i_index=len(tree1[0])-1-i
			j_index=len(tree2[0])-1-j
			if(len(tree1[1][i_index])*len(tree2[1][j_index])==0 or tree1[0][i_index].Type!=tree2[0][j_index].Type or tree1[2][i_index]!=tree2[2][j_index]):
				continue
			if(compute_if_preterminal_node(tree1,i_index)*compute_if_preterminal_node(tree2,j_index)==1):
				leaves_1=tree1[1][i_index]
				leaves_2=tree2[1][j_index]
				if (len(leaves_1)==len(leaves_2)):
					result=1
					for k in range(0,len(leaves_1)):
						node1=leaves_1[k]
						node2=leaves_2[k]
						if(tree1[0][node1].Type!=tree2[0][node2].Type):
							result=0
					tree_match_val[i_index][j_index]=result
					tree_match_val[i_index][j_index]=result

				else:
					pass
			else:
				if(compute_if_preterminal_node(tree1,i_index)*compute_if_preterminal_node(tree2,j_index)==1):
					leaves_1=tree1[1][i_index]
					leaves_2=tree2[1][j_index]
					if (len(leaves_1)==len(leaves_2)):
						result=1
						for k in range(0,len(leaves_1)):
							node1=leaves_1[k]
							node2=leaves_2[k]
							if(tree1[0][node1].Type!=tree2[0][node2].Type):
								result=0
						if(result==1):
							mult=1.0
							for k in range(0,len(leaves_1)):
								for l in range(0,len(leaves_1)):
									node1=leaves_1[k]
									node2=leaves_2[l]
									mult=mult*(delta+tree_match_val[node1][node2])
							tree_match_val[i_index][j_index]=mult
							tree_match_val[i_index][j_index]=mult
	sum_of_all_entries=0
	for item in tree_match_val:
		for val in item:
			sum_of_all_entries=sum_of_all_entries+val
	return sum_of_all_entries
if __name__ == '__main__':
	f=open("final_list_of_subexamples.pickle")
	#f=open("ex.pickle")
	obj=cPickle.load(f)
	f.close()
	K=[]
	for iter1 in range(0,len(obj)):
		lis_=[]
		for iter2 in range(0,len(obj)):
			print iter1,"===>",iter2
			lis_.append(compute_kernel(obj[iter1],obj[iter2],0.5))
		K.append(lis_)
	f=open("kernel_by_grammar_matching.pickle",'w')
	cPickle.dump(K,f)
	f.close