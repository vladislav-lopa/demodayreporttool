import re


class Regex():
    def allocate_time(self, name_of_card):
        self.name_of_card = name_of_card
        allocate_time = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', self.name_of_card)
        return allocate_time


def split_cards(report_tool):
    split_cards_from_list = "\n\t\t\t\t".join(report_tool)
    return split_cards_from_list
