import string


word_dict = {}

f = open('tweet_input/tweets.txt')
data = f.read()
words = data.split()
word_no_punctuation = []
for i in words:
	#i.replace(".", "")
	i = i.translate(string.maketrans("",""), string.punctuation)
	word_no_punctuation.append(i)
	word_dict[i] = word_no_punctuation.count(i)
	
print sorted(word_dict)

output = open('ft1.txt', 'w')

 
for i in sorted(word_dict): 
	output.write(i+'\t'+str(word_dict[i])+'\n')
	print i, word_dict[i]
output.close



#	words = []
#	i=i.strip()  
#	words=i.split() 

#for w in words:
    