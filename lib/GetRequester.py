import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        json_content = json.loads(self.get_response_body())
        return json_content

# programs = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
# print(programs)
# print(programs.get_response_body())
# print(programs.load_json())