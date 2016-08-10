#  File used to manual label the sub-examples

import cPickle
import kernel1
file_name=raw_input("Input file name:")
output=raw_input("Output file name:")
f=open(file_name)
list_of_obj=cPickle.load(f)
f.close()
y_label=[]
#obj=list_of_obj[0]
for obj in list_of_obj:
	nodes=obj[0]
	adjecency_list=obj[1]
	roles=obj[2]
	#print "nodes==>",nodes
	#print "adjecency_list==>",adjecency_list
	#print "roles==>",roles
	sentence=""
	for i in range(0,len(adjecency_list)):
		if(len(adjecency_list[i])==0):
			sentence=sentence+" "+nodes[i].Text
		if(roles[i]=="MEMBER"):
			member=nodes[i].Text
		if(roles[i]=="ORG"):
			org=nodes[i].Text
	print "sentence==>",sentence
	print "MEMBER==>",member
	print "ORGANISATION==>",org
	try:
		label=int(raw_input("Label 1 for positive and 0 for negative and -1 to terminate and 2 to ignore:"))
	except:
		label=int(raw_input("Label 1 for positive and 0 for negative and -1 to terminate and 2 to ignore(Is baar galti na karna):"))
	if(label==-1):
		break
	else:
		y_label.append(label)
f=open(output,'w')
list_of_obj=cPickle.dump(y_label,f)
f.close()