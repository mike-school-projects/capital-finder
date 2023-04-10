from urllib import parse
url_components = parse.urlsplit("https://capital-finder-mike.vercel.app/api/capital-finder?esaf=Santiago")
query_string_list = parse.parse_qsl(url_components.query)
dic = dict(query_string_list)
print(dic)

if "country" in dic:
    print("country")

elif "capital" in dic:
    print("capital")