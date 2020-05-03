import requests
import bs4
import lxml.etree as xml

url = "https://github.com/requests/requests"

response = requests.get(url)
# print(response)
# print(response.text)

web_page = bs4.BeautifulSoup(response.text, "lxml")
# print(web_page)

# print(web_page.head)

# print(web_page.head.title)

# print(web_page.head.title.text)

# print(web_page.body)

# sub_web_page = web_page.find_all(name="ul")
# print(sub_web_page)