import requests
import hashlib
import re

data=requests.get("https://ringzer0ctf.com/challenges/56", cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search("(?<=----- BEGIN HASH -----<br />\s\s\s\s)(.*)(?=<br />)", data).group(0)
for i in range(900,9000):
	if(hashlib.sha1(str(i)).hexdigest() == data):
		data = str(i)
		break
data=requests.get("https://ringzer0ctf.com/challenges/56/"+data,  cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search('(?<=<div class="alert alert-info">)(.*)(?=</div>)', data).group(0)
print(data)