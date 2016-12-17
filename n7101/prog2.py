testlist = ["sricharan"]
 
 
def gethandle(word):
    return ("").join(sorted(word))
 
 
anagrams={}
 
 
wordlist =open("words1")
for item in wordlist:
     handle = gethandle(item.strip())
     if handle not in anagrams:
         anagrams[handle] = [item.strip()]
     else:
         anagrams[handle].append(item.strip())
 
 
def testforanagrams(word):
    results = anagrams.get(gethandle(word),[])
 
 
    if len(results)>1:
          print word, ":",", ".join([item for item in results if item != word])
    else:
          print word, ":", "None"
 
 
map(testforanagrams,testlist)