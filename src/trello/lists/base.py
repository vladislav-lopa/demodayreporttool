import requests


from src.main.config import TrelloApi
from src.trello.lists.list import List


class ListOperation():
    def get_name_of_list(list_id):
        query = {
            'key': TrelloApi.key,
            'token': TrelloApi.token
        }

        response = requests.request(
            "GET",
            List.url_for_get_name_list(list_id),
            params=query
        )

        return response
