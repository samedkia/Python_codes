fname= input('enter file name: ')
file= open(fname)
lst=list()
for line in file:
    a=line.split()
    for i in range(len(a)):
        if a[i] in lst:
            continue
        else:
            lst.append(a[i])
lst.sort()
print(lst)
