from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path

        # Parses url.  Example:
        ## https://capital-finder-mike.vercel.app/api/capital-finder?test
        ## SplitResult(scheme='', netloc='', path='/api/capital-finder', query='test', fragment='')
        url_components = parse.urlsplit(s)

        # Pulls out query
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

        message = str(dic)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
