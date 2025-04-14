import re

sentence = """123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0"200 6248
 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"""

ip = re.search(r'^\d{1,3}(?:\.\d{1,3}){3}',sentence).group()
date = re.search(r'\[(.*?)\]',sentence).group(1)
image= re.search(r'GET \/pics\/\S+',sentence).group()
url = re.search(r'"(http[s]?://[^"]+)"',sentence).group(1)

print(ip)
print(date)
print(image)
print(url)