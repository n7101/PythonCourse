str1="sricharan"
str2="raincrash"
word1=[]
word2=[]
for x in range(len(str1)):
    word1.append(str1[x])
for y in range(len(str2)):
    word2.append(str2[y])
if(len(word1)==len(word2)):
    for letter in word1:
        if letter in word2:
            word2.remove(letter)

if len(word2)==0:
    print "anagram"
else:
    print "not anagram"
