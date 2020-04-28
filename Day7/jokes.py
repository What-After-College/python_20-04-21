import requests

url = "https://sv443.net/jokeapi/category/Programming?blacklistFlags=nsfwpolitical"

response = requests.get(url)
# print(response)
recieved_data = response.json()

# print(recieved_data)

# print(recieved_data['type'])

for x in recieved_data.keys():
    if x == 'id' or x=='warning':
        continue
    print("{} : {}".format(x, recieved_data[x]))

