import requests


from src.main.config import TrelloApi
from src.trello.boards.board import Board


class BoardOperation():
    def get_name_of_board(board_id):
        headers = {
           "Accept": "application/json"
        }

        query = {
           'key': TrelloApi.key,
           'token': TrelloApi.token
        }

        response = requests.request(
           "GET",
           Board.url_for_get_name_board(board_id),
           headers=headers,
           params=query
        )
        return response.json()["name"]