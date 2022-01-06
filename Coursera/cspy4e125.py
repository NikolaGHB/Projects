from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1402990.html"

html = urlopen(url, context=ctx).read()
parsed = BeautifulSoup(html, "html.parser")

comments = list()
total = list()

# Retrieve all of the anchor tags
spans = parsed('span')
for span in spans:
    print(span.contents[0])
    comments.append(span.contents[0])

for x in comments:
    total.append(int(x))

print(spans)
print(comments)
print(sum(total))
