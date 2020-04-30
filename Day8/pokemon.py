import requests
import json

def get_pokemon_data(name="Raichu"):
    url = "https://api.pokemontcg.io/v1/cards?name={}".format(name)
    response = requests.get(url)
    return response.json()

pokemon_name = input("Enter the name of the Pokemon: ")
recieved_data = get_pokemon_data(pokemon_name)   
# print(recieved_data['cards']) 

# import matplotlib.pyplot as plt

# url_data = requests.get(recieved_data["cards"][1]["imageUrl"])
# with open('./pika.png','wb') as f:
#     for item in url_data.iter_content(1024):
#         f.write(item)

# image_data = plt.imread('./pika.png')
# plt.imshow(image_data)
# plt.show()        

# import urllib.request
# import matplotlib.pyplot as plt

# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# urllib.request.install_opener(opener)

# urllib.request.urlretrieve(recieved_data['cards'][1]['imageUrl'], "00000001.png")

# image_data = plt.imread('./00000001.png')
# plt.imshow(image_data)
# plt.show()