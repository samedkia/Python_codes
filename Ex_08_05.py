fname= input('enter file name: ')
file= open(fname)
count=0
for line in file:
    if line.startswith('From '):
        ln= line.split()
        print(ln[1])
        count=count+1
    else:
        continue
print('There were',count, 'lines in the file with From as the first word')
