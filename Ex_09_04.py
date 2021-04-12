fname= input('enter file name: ')
file= open(fname)
dd={}
words=list()
for line in file:
    if line.startswith('From '):
        wordss=line.split()
        words.append(wordss[1])
for word in words:
    dd[word]= dd.get(word,0)+1
bigword=None
bigcount=None
for word,count in dd.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)
