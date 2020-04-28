import requests

url = "https://currencyapi.net/api/v1/rates?key=8S6WV4dEvTHzScNFZSscke0FRO7f8fEJbsFh"

response = requests.get(url)

recieved_data = response.json()

for data in recieved_data.keys():
    if data == 'rates':
        currency_rate = recieved_data[data]
        for ratesofMoney in currency_rate.keys():
            if ratesofMoney == "INR":
                print("Rate of Indian Rupees against one Dollar : {}".format(currency_rate[ratesofMoney]))

