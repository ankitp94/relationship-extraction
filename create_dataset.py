# File to convert the Google database to our use case of relationship extraction by anaphora resolution
import json
import cPickle
from nltk import tokenize
import urllib
from difflib import SequenceMatcher as SM
def create_dict_from_raw_dataset(string):
	dictionary=eval(string)
	snippet=dictionary["evidences"][0]["snippet"]
#	api_key= "XXXXX"
	service_url = 'https://www.googleapis.com/freebase/v1/topic'
	params = {
	  'key': api_key,
	  "filter":"suggest"
	}
	topic_id=dictionary["sub"]
	url = service_url + topic_id + '?' + urllib.urlencode(params)
	topic = json.loads(urllib.urlopen(url).read())
#	try:
	name=topic['property']["/type/object/name"]["values"][0]["text"]
#	except:
#		keys=[key in topic]
#		print keys
	topic_id=dictionary["obj"]
	url = service_url + topic_id + '?' + urllib.urlencode(params)
	topic = json.loads(urllib.urlopen(url).read())
	org=topic['property']["/type/object/name"]["values"][0]["text"]
	pseudo_list=tokenize.sent_tokenize(snippet.decode('utf-8'))
	sentence_list=[]
	for sentence in pseudo_list:
		words=sentence.split()
		pronouns=["He","She","he","she"]
		sent=""
		for word in words:
			if(word in pronouns):
				sent=sent+" "+name
			else:
				sent=sent+" "+word
		sent=sent[1:]
		sentence_list.append(sent)
	max_score=0
	for sentence in sentence_list:
		s=SM(None, sentence, org)
		score=sum(n for i,j,n in s.get_matching_blocks())
		if(score>max_score):
			max_score=score
			final_sentence=sentence
	yes_count=0
	no_count=0
	for judgment in dictionary["judgments"]:
		if(judgment["judgment"]=="yes"):
			yes_count=yes_count+1
		else:
			no_count=no_count+1
	if(yes_count>no_count):
		value=1
	else:
		value=0
	final_dictionary={}
	final_dictionary["value"]=value
	final_dictionary["sentence"]=final_sentence
	final_dictionary["name"]=name
	final_dictionary["organisation"]=org
	print final_dictionary
	return final_dictionary
if __name__ == "__main__":
	final_list_yes=[]
	final_list_no=[]
	with open("data.json") as f:
		contents = f.readlines()
	print len(contents)
	counter=0
	faulted=0
	yes=0
	no=0
	for line in contents:
		if(min(yes,no)>500):
			break
		try:
			dictionary = create_dict_from_raw_dataset(line[:-1])
			if(dictionary["value"]==1):
				final_list_yes.append(dictionary)
				yes=yes+1
			else:
				final_list_no.append(dictionary)
				no=no+1
		except:
			faulted=faulted+1
		counter=counter+1
		print "counter==>",counter
		print "faulted==>",faulted
		print "yes==>",yes
		print "no==>",no
		#except:
		#	break
	f = open('data_positive.pickle','w')
	cPickle.dump(final_list_yes,f)
	f.close()
	f = open('data_negative.pickle','w')
	cPickle.dump(final_list_no,f)
	f.close()
	print "dataset generated"