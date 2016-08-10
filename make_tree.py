from kernel1 import node

# class node(object):
# 	def __init__(self,type_,text):
# 		self.type_=type_
# 		self.text=text

def mk_tree(string):
	node_list=[]
	pseudo_adjcency_list=[]
	adjcency_list=[]
	new=string.replace("("," ( ")
	new_string=new.replace(")"," ) ")
	list_=new_string.split()
	bracket_count=0
	para_lis=['(',')']
	index_transformation={}
	for i in  range(0,len(list_)):
		item=list_[i]
		if(item=='('):
			bracket_count=bracket_count+1
		elif (item==')'):
			bracket_count=bracket_count-1
		if(item in para_lis):
			continue
		if(i>=1 and item not in para_lis and list_[i-1] not in para_lis):
			continue
		temp_bracket_count=1
		text=""
		list_of_edges=[]
		for temp_i in range(i+1,len(list_)):
			if(list_[temp_i]=='('):
				temp_bracket_count=temp_bracket_count+1
			elif (list_[temp_i]==')'):
				temp_bracket_count=temp_bracket_count-1
			if(temp_bracket_count==0):
				break
			if(list_[temp_i] not in para_lis and list_[temp_i-1] not in para_lis):
				text=text+" "+list_[temp_i]
			elif(list_[temp_i] not in para_lis and temp_bracket_count==2):
				list_of_edges.append(temp_i)
		temp_node=node(item,text)
		node_list.append(temp_node)
		index_transformation[i]=len(node_list)-1
		pseudo_adjcency_list.append(list_of_edges)
	for adj_lis in pseudo_adjcency_list:
		lis_=[]
		for key in adj_lis:
			lis_.append(index_transformation[key])
		adjcency_list.append(lis_)
	return (node_list,adjcency_list)

if __name__ == '__main__':
	string="(ROOT (S (NP (NNP John) (NNP Smith)) (VP (VBZ is) (NP (NP (DT a) (NN scientist)) (PP (IN at) (NP (NNP Harvard))))) (. .)))"
	r=mk_tree(string)
	node_list=r[0]
	adjcency_list=r[1]
	print string
	for i in range(0,len(node_list)):
		print i,"==>",node_list[i].Type,"==>",node_list[i].Text
		print adjcency_list[i]