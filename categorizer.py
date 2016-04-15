from nltk.corpus import wordnet
from operator import itemgetter
from itertools import product
import pickle

aspects=pickle.load(open('aspect_dump_new.p','rb'))
#print aspects
# l= [u'vodka', u'vodka', u'cocktail']
list1=[u'food', u'ambience', u'price', u'anecdotes/miscellaneous', u'service']
cats_dict={}
for sid in aspects.keys():
	l=aspects[sid]
	similarities=[]
	inner=[]
	categories=[]
	for asp in l:
		print asp
		inner=[]
		sense1=wordnet.synsets(asp)
		#print "sense1:",sense1
		for cat in list1:
			print cat
			sense2=wordnet.synsets(cat)
			#print "sense2",sense2
			for s1,s2 in product(sense1,sense2):
				score=wordnet.wup_similarity(s1,s2)
				# print score,s1,s2
				inner.append((score,s2))
		print "\n"
		if len(inner)>0:
			topcat=sorted(inner,key=itemgetter(0),reverse=True)[0]
			categories.append(topcat[1].name()[:topcat[1].name().index('.')])
	cats_dict[sid]=list(set(categories))
print cats_dict
pickle.dump(cats_dict,open('cats_dump.p','wb'))

