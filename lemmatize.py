from nltk.stem.wordnet import WordNetLemmatizer
import pickle

sentence=pickle.load(open('new_file.p','rb'))

lmt=WordNetLemmatizer()

inenr={}
ml=[]
for key in sentence.keys():
	inner=sentence[key]
	for ikey in inner.keys():
		x=lmt.lemmatize(ikey)
		inner[x]=inner.pop(ikey)
	sentence[key]=inner

print sentence
pickle.dump(sentence,open('new_file.p','wb'))

