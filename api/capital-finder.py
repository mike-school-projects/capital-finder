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

        # dic = dict(query_string_list)

        # Base URL
        url = "https://restcountries.com/v3.1/name/"

        # Get data from API using base URL plus country
        r = requests.get(url + query_string_list)

        # Get data from API as json
        data = r.json()

        message = str(data)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
