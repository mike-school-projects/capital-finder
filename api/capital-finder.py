from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import logging

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path

        # Parses url.  Example:
        ## https://capital-finder-mike.vercel.app/api/capital-finder?test
        ## SplitResult(scheme='', netloc='', path='/api/capital-finder', query='test', fragment='')
        url_components = parse.urlsplit(s)
        logging.warning(f'url_components: {url_components}')

        # Pulls out query
        query_string_list = parse.parse_qsl(url_components.query)
        logging.warning(f'query_string_list: {query_string_list}')

        dic = dict(query_string_list)
        logging.warning(f'dic: {dic}')

        # Base URL
        url = "https://restcountries.com/v3.1/name/"

        # Get data from API using base URL plus country
        # r = requests.get(url + query_string_list)
        # logging.warning(f'r: {r}')

        # Get data from API as json
        # data = r.json()
        # logging.warning(f'data: {data}')

        # message = str(query_string_list)

        message = "test"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
