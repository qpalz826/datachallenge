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
for line in f:
	array.append(line)
print array
f.close()
for sentence in array:
	words = sentence.split()
	number.append(len(list(set(words))))
	print number
	print median(number)
