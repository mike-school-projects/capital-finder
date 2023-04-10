from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        # Parses url.  Example:
        ## https://capital-finder-mike.vercel.app/api/capital-finder?test
        ## SplitResult(scheme='', netloc='', path='/api/capital-finder', query='test', fragment='')
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # Query by country
        if "country" in dic:
            # Produces good URL
            url = "https://restcountries.com/v3.1/name/" + dic["country"]

            # Get data from API
            # Produces 200 status code
            response = requests.get(url)

            # convert to json
            # Produces good data
            data = response.json()

            # Parse out capital
            capital = data[0]['capital'][0]

            message = f'The capital of {dic["country"]} is {capital}'

        # Query by capital
        elif "capital" in dic:
            # Produces good URL
            url = "https://restcountries.com/v3.1/name/" + dic["capital"]

            # Get data from API
            # Produces 200 status code
            response = requests.get(url)

            # convert to json
            # Produces good data
            data = response.json()

            # Parse out capital
            capital = data[0]['capital'][0]

            message = f'The capital of {dic["country"]} is {capital}'
            message = str(url)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
