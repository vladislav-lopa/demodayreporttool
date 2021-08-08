import logging


from src.trello.сards.base import CardOperation
from src.main.config import ListID


class StoryPointOperation(CardOperation):
    def all_calculate():
        try:
            time_todo_list = (CardOperation(ListID.todo_id).
                              get_sum_of_cards())
            time_in_progress_list = (CardOperation(ListID.in_progress_id).
                                     get_sum_of_cards())
            time_code_review_list = (CardOperation(ListID.code_review_id).
                                     get_sum_of_cards())
            time_in_test_list = (CardOperation(ListID.in_test_id).
                                 get_sum_of_cards())
            time_release_list = (CardOperation(ListID.release_id).
                                 get_sum_of_cards())
            time_done_list = (CardOperation(ListID.done_id).
                              get_sum_of_cards())

            total_time = (
                    time_todo_list +
                    time_in_progress_list +
                    time_code_review_list +
                    time_in_test_list +
                    time_release_list +
                    time_done_list
            )
            return total_time
        except IndexError:
            logging.basicConfig(filename="../../main/log/exception.log", filemode="w")
            logging.error("Don't have time on card")
            print("Please enter time on card")

    def done_calculate():
        try:
            time_done_list = (CardOperation(ListID.done_id).
                              get_sum_of_cards())
            return time_done_list
        except IndexError:
            logging.basicConfig(filename="../../main/log/exception.log", filemode="w")
            logging.error("Don't have time on card")
            print("Please enter time on card")

    def release_calculate():
        try:
            time_release_list = (CardOperation(ListID.release_id).
                                 get_sum_of_cards())
            return time_release_list
        except IndexError:
            logging.basicConfig(filename="../../main/log/exception.log", filemode="w")
            logging.error("Don't have time on card")
            print("Please enter time on card")
