str1 = "this is srinivas  srinivas is a trainer"
words=str1.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)
