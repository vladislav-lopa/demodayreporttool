from src.trello.lists.base import ListOperation


def name_list(list_id, list):
    name_list = ListOperation.get_name_of_list(list_id)
    assert name_list.json()["name"] == list, "List name do not match"