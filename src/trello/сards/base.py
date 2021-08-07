import requests


from src.main.config import TrelloApi
from src.main.utils import Regex
from src.trello.сards.card import Card


class CardOperation():
    def __init__(self, input_id):
        "Get id all cards in list"
        query = {
            'key': TrelloApi.key,
            'token': TrelloApi.token
        }
        self.response = requests.request(
            "GET",
            Card.url_for_get_id_card(input_id),
            params=query
        )

    def get_name_of_card(self):
        "Get all names cards from list"
        list_for_name_cards = []
        list_id = self.response.json()
        for i in range(len(list_id)):
            list_id = self.response.json()[i]["id"]

            headers = {
                "Accept": "application/json"
            }

            query = {
                'key': TrelloApi.key,
                'token': TrelloApi.token
            }

            response_for_name_card = requests.request(
                "GET",
                Card.url_for_get_name_card(list_id),
                headers=headers,
                params=query
            )

            name_of_card = response_for_name_card.json()["name"]

            card_without_time = name_of_card.replace(Card.url_for_get_time_on_card(self, name_of_card), ' ')
            list_for_name_cards.append(card_without_time)
        return list_for_name_cards

    def get_sum_of_cards(self):
        "Get all sum of time from cards"
        list_for_time = []
        len_of_list = self.response.json()
        for i in range(len(len_of_list)):
            list_id = self.response.json()[i]["id"]

            headers = {
                "Accept": "application/json"
            }
            query = {
                'key': TrelloApi.key,
                'token': TrelloApi.token
            }

            response_for_name_card = requests.request(
                "GET",
                Card.url_for_get_name_card(list_id),
                headers=headers,
                params=query
            )

            card_name = response_for_name_card.json()["name"]

            time = float(Regex.allocate_time(self, card_name)[-1])
            list_for_time.append(time)
        return sum(list_for_time)
