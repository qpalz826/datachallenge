import string
def median(a):
    """Return the median of sequence a."""
    a = sorted(a)
    length = len(a)
    if length == 1:
    	return a[0]
    elif length % 2 == 1:
        return a[length/2]
    else:
        return (a[length/2] + a[length/2 - 1]) / 2.0


f = open('tweet_input/tweets.txt')

array = []
number =[]
words_no_punctuation = []
c = []

output = open('tweet_output/ft2.txt', 'w')

for line in f:
	array.append(line)

f.close()

for sentence in array:
	sentence = sentence.translate(string.maketrans("",""), string.punctuation) # "?,." can also be string.punctuation to include all the punctuation
	words = sentence.split()
	number.append(len(list(set(words))))
	output.write(str(median(number))+'\n')
output.close()