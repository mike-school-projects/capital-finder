from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        # Parses url
        url_components = parse.urlsplit(path)

        # Converts query parameter to a pair of strings
        query_string_list = parse.parse_qsl(url_components.query)

        # Converts to a dictionary
        dic = dict(query_string_list)

        try:
            # Query by country
            if "country" in dic:
                url = "https://restcountries.com/v3.1/name/" + dic["country"]

                # Get data from API
                response = requests.get(url)

                # convert to json
                data = response.json()

                # Parse out capital
                capital = data[0]['capital'][0]

                message = f'The capital of {dic["country"]} is {capital}'

            # Query by capital
            elif "capital" in dic:
                url = "https://restcountries.com/v3.1/capital/" + dic["capital"]

                # Get data from API
                response = requests.get(url)

                # convert to json
                data = response.json()

                # Parse out country
                country = data[0]['name']['common']

                message = f'The capital of {country} is {dic["capital"]}'

            # If query is something other than capital or country
            else:
                message = "Need more info.  Query for capital or country"

        # If website error
        except:
            message = "Bad info.  Too bad, so sad"

        # If request returns an empty response
        if message == '':
            message = "Need more info.  Query for capital or country"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
