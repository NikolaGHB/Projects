import re
name = input("Enter file name:")
if len(name) < 1:
    name ="regex_sum_1402988.txt"

handle = open(name)

sumt = list()
tsum = None

for line in handle:
    z = re.search("[0-9]+", line)
    if z is None:
        continue
    else:
        lsum = re.findall("[0-9]+", line)
        for x in lsum:
            sumt.append(int(x))

tsum = sum(sumt)

print(tsum)
