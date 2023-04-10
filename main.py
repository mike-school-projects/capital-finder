from urllib import parse
import requests

url_components = parse.urlsplit("https://capital-finder-mike.vercel.app/api/capital-finder?capital=Chile")
query_string_list = parse.parse_qsl(url_components.query)
dic = dict(query_string_list)

url = "https://restcountries.com/v3.1/name/" + dic["capital"]
data = requests.get(url)
data = data.json()
country = data[0]['name']['common']
print(country)


# print(data[0]['capital'][0])
# for word_data in data:
#     for word in word_data:
#         print(word)
#         input("wait")
