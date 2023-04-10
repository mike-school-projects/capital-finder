from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            # url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

            # Base URL
            url = "https://restcountries.com/v3.1/name/"

            # Full URL with endpoint
            r = requests.get(url + dic["word"])

            # Get data from API as json
            data = r.json()

            with open("test.json", "w") as file:
                file.write(data)

            #
            capital = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                capital.append(definition)
            message = str(capital)

        else:
            message = "Give me a word to define please"

        message = "here"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
