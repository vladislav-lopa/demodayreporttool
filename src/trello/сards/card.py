from src.main.utils import Regex


class Card():
    def url_for_get_id_card(input_id):
        get_id_card = f"https://api.trello.com/1/lists/{input_id}/cards"
        return get_id_card

    def url_for_get_name_card(input_id):
        get_name_card = f"https://api.trello.com/1/cards/{input_id}"
        return get_name_card

    def url_for_get_time_on_card(self, name_of_card):
        remove_time = "(" + str(Regex.allocate_time(self, name_of_card)[-1]) + ")"
        return remove_time
