import requests
import hashlib
import re

data=requests.get("https://ringzer0ctf.com/challenges/14", cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search("(?<=----- BEGIN MESSAGE -----<br />\s\s\s\s)(.*)(?=<br />)", data).group(0)

groups=[]
group=""
done_till=0
for k in list(data):
	group+=k
	if(done_till==7):
		groups.append(group)
		group=""
		done_till=-1
	done_till+=1

message = ""
for b in groups:
	message += chr(int(b,2))

data = message

data=requests.get("https://ringzer0ctf.com/challenges/14/"+hashlib.sha512(data).hexdigest(),  cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search('(?<=<div class="alert alert-info">)(.*)(?=</div>)', data).group(0)

print(data)

