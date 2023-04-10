from urllib import parse
import requests

url_components = parse.urlsplit("https://capital-finder-mike.vercel.app/api/capital-finder?country=Chile")
query_string_list = parse.parse_qsl(url_components.query)
dic = dict(query_string_list)

url = "https://restcountries.com/v3.1/name/" + dic["country"]
data = requests.get(url)
data = data.json()
print(data[0]['capital'])
# for word_data in data:
#     for word in word_data:
#         print(word)
#         input("wait")
