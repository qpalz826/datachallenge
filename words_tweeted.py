import string


word_dict = {}

f = open('tweet_input/tweets.txt')
data = f.read()
words = data.split()
word_no_punctuation = []

for i in words:
#strip the punctuation "?,." from the text, if you want to strip all the punctuation, use string.punctuation instead of "?,." I didn't do that so as to have the same ft1.txt output as the example repo
	i = i.translate(string.maketrans("",""), "?, .")  
	word_no_punctuation.append(i)
	word_dict[i] = word_no_punctuation.count(i)
	

output = open('tweet_output/ft1.txt', 'w')
 
for i in sorted(word_dict): 
	output.write(i+'\t'+str(word_dict[i])+'\n')
	print i, word_dict[i]
output.close
f.close

