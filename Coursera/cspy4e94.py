name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
incoming = dict()
sender_list = list()

for line in handle:
    if not line.startswith("From"):
        continue
    elif line.startswith("From:"):
        continue
    else:
        send_line = line.split()
        sender = send_line[1]
        sender_list.append(sender)

for sent in sender_list:
    incoming[sent] = incoming.get(sent, 0) + 1

times_sent = None
committer = None

for x,y in incoming.items():
    if times_sent is None or y > times_sent:
        committer = x
        times_sent = y

print(committer, times_sent)
