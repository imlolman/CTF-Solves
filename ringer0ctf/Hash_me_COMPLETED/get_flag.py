import requests
import hashlib
import re

data=requests.get("https://ringzer0ctf.com/challenges/13", cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search("(?<=----- BEGIN MESSAGE -----<br />\s\s\s\s)(.*)(?=<br />)", data).group(0)

data=requests.get("https://ringzer0ctf.com/challenges/13/"+hashlib.sha512(data).hexdigest(),  cookies={"PHPSESSID": "qihrrs0aumntnnv7a7gpatjsh1"}).text
data=re.search('(?<=<div class="alert alert-info">)(.*)(?=</div>)', data).group(0)
print(data)