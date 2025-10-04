import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)

result = requests.get(url)
print(f'STATUS CODE: {result.status_code}')
print(f'JSON BODY: {result.json()}')
print(f'HEADERS: {result.headers}')
print('-------------------------')
assert result.status_code == 200

if result.status_code == 200:
    print('Everything is ok 200')
else:
    print('Error request!')
