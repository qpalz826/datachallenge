import string
words = ["I love you!", "I hate you", "hello."]
words_no_punctuation=[]
for i in words:
	i = i.translate(string.maketrans("",""), string.punctuation)
	words.append(i)
print words_no_punctuation
print words