# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File does not exist or cannot be opened:", fname)
    quit()
#counting variable
count = 0
cfdot = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        #finding value and slicing
        dot = line.find(".")
        fdot = float(line[dot-1:dot+5])
        #counting, adding values and finding result
        count = count + 1
        cfdot = cfdot + fdot
        result = float(cfdot/count)

print("Average spam confidence:",result)
