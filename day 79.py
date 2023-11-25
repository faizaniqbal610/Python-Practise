import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "tital":"Faizan",
    "body":"bhai",
    "userId":"15"
}

headers = {
    'Content-type':"application/json; charset=UTF-8"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
