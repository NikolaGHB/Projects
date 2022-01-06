name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
incoming = dict()
sender_list = list()

inh = dict()
senh = list()

for line in handle:
    if not line.startswith("From"):
        continue
    elif line.startswith("From:"):
        continue
    else:
        send_line = line.split()
        sender = send_line[1]
        sender_list.append(sender)
        time = send_line[5]
        hour = time[:2]
        senh.append(hour)

for t in senh:
    inh[t] = inh.get(t, 0) + 1

for k, v in sorted(inh.items()):
    print(k, v)

for sent in sender_list:
    incoming[sent] = incoming.get(sent, 0) + 1

times_sent = None
committer = None

for x,y in incoming.items():
    if times_sent is None or y > times_sent:
        committer = x
        times_sent = y

#print(committer, times_sent)
