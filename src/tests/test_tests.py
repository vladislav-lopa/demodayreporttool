from src.main.config import ListID
from src.trello.lists.base import ListOperation
from src.tests.templates import name_list


def test_connection():
    status = ListOperation.get_name_of_list(ListID.todo_id).status_code
    assert status == 200, "Don't have connection with trello"


def test_lists():
    name_list(ListID.todo_id, "TODO")
    name_list(ListID.in_progress_id, "IN PROGRESS")
    name_list(ListID.code_review_id, "CODE REVIEW")
    name_list(ListID.in_test_id, "IN TEST")
    name_list(ListID.release_id, "RELEASE")
    name_list(ListID.done_id, "DONE")