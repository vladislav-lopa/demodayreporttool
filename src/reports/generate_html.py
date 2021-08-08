from src.main.config import ListID
from src.trello.сards.base import CardOperation
from src.trello.lists.base import ListOperation
from src.trello.сards.advanced import StoryPointOperation
from src.main.utils import split_cards
from src.trello.boards.base import BoardOperation
from src.main.config import BoardID


class ReportTool():
    def __init__(self, list_id):
        self.all_cards_on_list = CardOperation(list_id).get_name_of_card()
        self.list_title = []
        self.list_title.extend([ListOperation.get_name_of_list(list_id).json()["name"]]
                               * len(self.all_cards_on_list))

    def list_of_cards_with_status(self):
        list_of_cards_with_status = []
        for i in range(len(self.all_cards_on_list)):
            card_name = self.all_cards_on_list[i]
            card_status = self.list_title[i]
            card_color = "green" if card_status == "DONE" else "orange"
            card_with_status = f"<li><strong>{card_name}</strong> " \
                               f"<span class='card-label card-label-black mod-card-detail-{card_color}'> " \
                               f"<span class='label-text'>{card_status}</span></span></li>"
            list_of_cards_with_status.append(card_with_status)
        return list_of_cards_with_status


class Category(ReportTool):
    def unfinished():
        cards_in_first_category = f"<h1 class='top-indent'> What we don't do: </h1>" \
                                  + split_cards(ReportTool(
            ListID.todo_id).list_of_cards_with_status()) \
                                  + split_cards(ReportTool(
            ListID.in_progress_id).list_of_cards_with_status()) \
                                  + split_cards(ReportTool(
            ListID.code_review_id).list_of_cards_with_status()) \
                                  + split_cards(ReportTool(
            ListID.in_test_id).list_of_cards_with_status())
        return cards_in_first_category

    def task_in_release():
        cards_in_second_category = "\n\t\t\t\t" f"<h1 class ='top-indent'>Task in release: </h1>" \
                                   + split_cards(ReportTool(
            ListID.release_id).list_of_cards_with_status())
        return cards_in_second_category

    def completed():
        cards_in_third_category = "\n\t\t\t\t"f"<h1 class='top-indent'>What we done: </h1>" \
                                  + split_cards(ReportTool(
            ListID.done_id).list_of_cards_with_status())
        return cards_in_third_category

    def count_story_points_by_categories():
        count_all_and_done_story_points = "\n\t\t\t\t"f"<h1 class='top-indent'>Total time: </h1>" \
                                          "\n\t\t\t\t"f"<li><strong>Summary:{StoryPointOperation.all_calculate()}/" \
                                          "\n\t\t\t\t"f"{StoryPointOperation.done_calculate()}" \
                                          "\n\t\t\t\t"f"(All time/Done)</strong></li>" \
                                          "\n\t\t\t\t"f"<li><strong>Waiting for deploy:" \
                                          "\n\t\t\t\t"f"{StoryPointOperation.release_calculate()}</strong> </li>"
        return count_all_and_done_story_points

    def sprint_name():
        board_name = "\n\t\t\t\t"f"<h1 class='top-indent'>" \
                     f"{BoardOperation.get_name_of_board(BoardID.board_id)}</h1>"
        return board_name


class GenerateReport(ReportTool):
    def generate_full_report(imput_content, name_slide, previous_page, next_page):
        html_content = f"<html>" "\n\t" \
                       f"<head>" "\n\t\t" \
                       f"<link href='https://fonts.googleapis.com/css2?family=Jura&display=swap' rel='stylesheet'>""\n\t\t" \
                       f"<link href='https://fonts.googleapis.com/css2?family=Alegreya+Sans+SC&display=swap' rel='stylesheet'> " "\n\t\t" \
                       f"<link href = 'https://fonts.googleapis.com/css2?family=Krona+One&display=swap' rel ='stylesheet'> ""\n\t\t" \
                       f"<link rel='stylesheet' href='../style.css'>" "\n\t\t" \
                       f"<meta charset = 'utf-8'>""\n\t\t" \
                       f"<meta name = 'viewport' content = 'width=device-width, initial-scale=1'>""\n\t\t" \
                       f"<link href = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css'rel = 'stylesheet'""\n\t\t" \
                       f"integrity = 'sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6'crossorigin = 'anonymous'>""\n\t" \
                       f"</head> ""\n\t\t" \
                       f"<body> " "\n\t\t\t" \
                       f"<center>""\n\t\t\t\t" \
                       f"<div class ='make-container'>""\n\t\t\t\t\t" \
                       f"<nav class ='navbar navbar-expand-lg navbar-light bg-light'>""\n\t\t\t\t\t\t" \
                       f"<div class ='container-fluid'>""\n\t\t\t\t\t\t\t" \
                       f"<div class ='collapse navbar-collapse' id='navbarSupportedContent'>""\n\t\t\t\t\t\t\t" \
                       f"<ul class ='navbar-nav me-auto mb-2 mb-lg-0'>" "\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button'>""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>" "\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active' aria-current='page' href='sprint_name.html'>""\n\t\t\t\t\t\t\t" \
                       f" <strong>Sprint</strong></a>""\n\t\t\t\t\t\t\t" \
                       f"</li></button>""\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button'>""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>""\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active ' aria-current='page' href='completed.html'>""\n\t\t\t\t\t\t\t" \
                       f" What we done </a>""\n\t\t\t\t\t\t\t" \
                       f"</li>""\n\t\t\t\t\t\t\t" \
                       f"</button>""\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button'>""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>""\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active' aria-current='page' href='task_in_release.html'>""\n\t\t\t\t\t\t\t" \
                       f"Tasks in release </a>""\n\t\t\t\t\t\t\t" \
                       f"</li>""\n\t\t\t\t\t\t\t" \
                       f"</button>""\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button' >""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>""\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active' aria-current='page' href='unfinished.html'> ""\n\t\t\t\t\t\t\t" \
                       f"What we don't do</a>""\n\t\t\t\t\t\t\t" \
                       f"</li>""\n\t\t\t\t\t\t\t" \
                       f"</button>""\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button'>""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>""\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active' aria-current='page' href='total_story_points.html'>" "\n\t\t\t\t\t\t\t" \
                       f" Time for sprint </a>""\n\t\t\t\t\t\t\t" \
                       f"</li> </button>""\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button'>""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>""\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active' aria-current='page' href='planing_to_do.html'>""\n\t\t\t\t\t\t\t" \
                       f" What we want to do next sprint </a>""\n\t\t\t\t\t\t\t" \
                       f"</li></button>""\n\t\t\t\t\t\t\t" \
                       f"<button class ='btn btn-sm btn-outline-secondary' type='button'>""\n\t\t\t\t\t\t\t" \
                       f"<li class ='nav-item'>""\n\t\t\t\t\t\t\t" \
                       f"<a class ='nav-link active' aria-current='page' href='questions.html'>""\n\t\t\t\t\t\t\t" \
                       f" Questions </a>""\n\t\t\t\t\t\t\t" \
                       f"</li>""\n\t\t\t\t\t\t" \
                       f"</button>""\n\t\t\t\t\t\t" \
                       f"</ul>""\n\t\t\t\t\t" \
                       f"</div>""\n\t\t\t\t" \
                       f"</div>""\n\t\t\t" \
                       f"</nav>""\n\t\t" \
                       f"</div>""\n\t" \
                       f"</center>""\n\t" \
                       f"<div lass ='container-xl center'>""\n\t\t" \
                       f"<center>""\n\t\t\t" \
                       f"<div class ='col-4'>" \
                       f"{imput_content}" \
                       f"<button class ='carousel-control-prev' type='button' data-bs-target='#carouselExampleDark' data-bs-slide='../page1.html'>""\n\t\t\t\t" \
                       f"<a href='{previous_page}.html' class ='carousel-control-prev-icon' aria-hidden='true'></a>""\n\t\t\t\t" \
                       f"<span class ='visually-hidden' href='page1.html'>Previous</span>""\n\t\t\t\t" \
                       f"</button>""\n\t\t\t\t" \
                       f"<button class ='carousel-control-next' type='button'  data-bs-slide='../page1.html'>""\n\t\t\t\t" \
                       f"<a href='{next_page}.html' class ='carousel-control-next-icon' aria-hidden='true'></a>""\n\t\t\t\t" \
                       f"<span class ='visually-hidden'>Next</span>""\n\t\t\t\t" \
                       f"</button>""\n\t\t\t" \
                       f"</div>""\n\t\t" \
                       f"</center>""\n\t" \
                       f"</div>""\n\t" \
                       f"<script src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js' integrity = 'sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf' crossorigin = 'anonymous'> </script>""\n\t" \
                       f"<script src = 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js' integrity = 'sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG' crossorigin = 'anonymous'> </script>""\n\t" \
                       f"<script src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js' integrity = 'sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc' crossorigin = 'anonymous'> </script>""\n\t" \
                       f"</body>""\n" \
                       f"</html>"

        with open(f"{name_slide}.html", "w", encoding="utf-8") as html_file:
            html_file.write(html_content)


class Pages():
    def generate_pages():
        GenerateReport.generate_full_report(Category.unfinished(),
                                            'src/main/presentation/pages/unfinished',
                                            'task_in_release',
                                            'total_story_points')
        GenerateReport.generate_full_report(Category.task_in_release(),
                                            'src/main/presentation/pages/task_in_release',
                                            'completed',
                                            'unfinished')
        GenerateReport.generate_full_report(Category.completed(),
                                            'src/main/presentation/pages/completed',
                                            'sprint_name',
                                            'task_in_release')
        GenerateReport.generate_full_report(Category.count_story_points_by_categories(),
                                            'src/main/presentation/pages/total_story_points',
                                            'unfinished',
                                            'planing_to_do')
        GenerateReport.generate_full_report(Category.sprint_name(),
                                            'src/main/presentation/pages/sprint_name',
                                            '#',
                                            'completed')
        GenerateReport.generate_full_report('<h1 class="top-indent">What we want to do on next sprint</h1>',
                                            'src/main/presentation/pages/planing_to_do',
                                            'total_story_points',
                                            'questions')
        GenerateReport.generate_full_report('<h1 class="top-indent">Questions</h1>',
                                            'src/main/presentation/pages/questions',
                                            'planing_to_do',
                                            '#')
        print("html file created successfully !!")
