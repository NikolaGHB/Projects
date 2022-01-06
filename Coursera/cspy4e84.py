fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File does not exist or cannot be opened:", fname)
    quit()

lst = list()
word = list()

for line in fh:
    line = line.split()
    for x in line:
        word.append(x)

for x in word:
    if x not in lst:
        lst.append(x)
lst.sort()
print(lst)
