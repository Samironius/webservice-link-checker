from urllib.parse import urlparse
import sqlite3
import re

class Policy:

    def __init__(self, url):
        self.url = url

    def compare_urls(self, url1, url2):
        url1_parsed = urlparse(url1.rstrip("/"))
        url2_parsed = urlparse(url2.rstrip("/"))

        comparisons = ["scheme", "hostname", "path"]
        for attr in comparisons:
            if getattr(url1_parsed, attr) != getattr(url2_parsed, attr):
                return False

        ports = [url1_parsed.port, url2_parsed.port]
        comparisons = [url1_parsed, url2_parsed]
        for index, url in enumerate(comparisons):
            if url.port is None and url.scheme == "http":
                ports[index] = 80
            elif url.port is None and url.scheme == "https":
                ports[index] = 443

        if ports[0] != ports[1]:
            return False

        return True 

    def read_db(self):
        regex = "\'(.*?)\'"
        conn = sqlite3.connect('my.db')
        c = conn.cursor()
        urls = c.execute('SELECT url FROM urls').fetchall()
        policy = c.execute('SELECT policy FROM urls').fetchall()
        return dict(zip(re.findall(regex, str(urls)), re.findall(regex, str(policy))))

    def finde_in_db(self):

        for x in self.read_db():
            if self.compare_urls(x, self.url) == True:
                return self.read_db()[x]
        return "blocked"
