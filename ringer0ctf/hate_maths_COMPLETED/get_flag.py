import requests
import hashlib
import re

data=requests.get("https://ringzer0ctf.com/challenges/32", cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text

data=re.search("(?<=----- BEGIN MESSAGE -----<br />\s\s\s\s)(.*)(?=<br />)", data).group(0)
data=re.search("(.*)(?== ?)",data).group(0)

data=data.replace("- ","- 0b")
data=str(eval(data))
data=requests.get("https://ringzer0ctf.com/challenges/32/"+data,  cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search('(?<=<div class="alert alert-info">)(.*)(?=</div>)', data).group(0)
print(data)