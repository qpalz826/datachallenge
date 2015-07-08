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

list_per_tweet = []
f = open('tweet_input/tweets.txt')
data = f.read()
words = data.split()
for i in words:
	i = i.translate(string.maketrans("",""), string.punctuation)
	word_no_punctuation.append(i)
	word_dict[i] = word_no_punctuation.count(i)
	
for array in words:
	x = words.count(array)
	list_per_tweet.append(x)
print list_per_tweet
	
print "median:", median(list_per_tweet)