import re
fname= input('enter file name: ')
file= open(fname)
lst= list()
for line in file:
    line= line.rstrip()
    a= re.findall('[0-9]+', line)
    lst= lst+a
for i in range(len(lst)):
    lst[i]= int(lst[i])
x= sum(lst)
print(x)
