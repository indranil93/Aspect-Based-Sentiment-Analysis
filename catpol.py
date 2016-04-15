import pickle
import a
import sys
from nltk.stem.wordnet import WordNetLemmatizer

lem=WordNetLemmatizer()

sentic=pickle.load(open('sentic_dump.p','rb'))			#sentnic dictionary
sentence=pickle.load(open('sentence_dump.p','rb'))		#parser output dictionary
sentword=pickle.load(open('sentiword_dump.p','rb'))		#sentiwordnet dictionary
aspect=pickle.load(open('aspect_dump_new.p', 'rb'))			#aspect_term extractor dictionary
adav=["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
polarit=pickle.load(open('polarities.p','rb'))
cat=pickle.load(open('new_file.p','rb'))
nnegative = ['not', 'Not', "n't"]
noun = ["NN", "NNS", "NNP", "NNPS"]
positive =1
negative = -1
neutral=0 
#print polarit
polcat_dict={}
def extractor(words = {}, sid=0):				#sid = sentence id, and words = aspect terms 
	#print sid	
	print words
	inner={}
	#print words
	for j in words:						# one by one aspect terms theeskuntam
		lit={}
		p='neutral'
		# print j
		print polarit[sid]
		if lem.lemmatize(j) in polarit[sid].keys():						#j is the aspect term 
	 		p= polarit[sid][lem.lemmatize(j)]#,'adfaaafadfasdf'
	 	if j in polarit[sid].keys():
	 		p= polarit[sid][j]
	 #   print p
	 	for l in words[j]:
			print l
			lit[l]=p
		#print lit[l]
		inner[j]=lit
	    #print inner[j]
	polcat_dict[sid]=inner#print polcat_dict[sid]

if __name__ == "__main__":
    #words = {}
#    words = {"word" : {"pos_tag" : "verb"},}
	for sid in cat.keys():				#aspect dictionary lo key sentence id and value aa sentence lo unna aspect terms
    #get words as dictionary #graph
		#print sid
            #subNoun = isNounSubject(sentence[sid])
		extractor(cat[sid], sid)			#one by one sentence id pampistam
        #print polcat_dict
	pickle.dump(polcat_dict,open('polcat.p','wb'))
	

