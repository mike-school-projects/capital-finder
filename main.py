from urllib import parse
url_components = parse.urlsplit("https://capital-finder-mike.vercel.app/api/capital-finder?country=Santiago")
query_string_list = parse.parse_qsl(url_components.query)
dic = dict(query_string_list)
print(dic)

if "country" in dic:
    url = "https://restcountries.com/v3.1/name/" + dic["country"]
    print(url)

elif "capital" in dic:
    print("capital")