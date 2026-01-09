import base64, urllib.parse

data_url_encoded_xor_jsonencoded="HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"

data_encoded_xor_jsonencoded=urllib.parse.unquote(data_url_encoded_xor_jsonencoded)

data_xor_jsonencoded=base64.b64decode(data_encoded_xor_jsonencoded).decode()

n=len(data_xor_jsonencoded)
print(n)


key=""

for i in range(n):
    print(data_xor_jsonencoded[i]^)

print(data_encoded_xor_jsonencoded)
print(data_xor_jsonencoded)