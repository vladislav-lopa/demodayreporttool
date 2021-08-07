# Deployment :
- Install and configure [Python3](https://www.python.org/downloads/)
- Import cloned repository:
  ```
  git clone https://github.com/vladislav-lopa/demodayreporttool.git
  ```
- Install all required packages using this command:
    ```sh
    pip install -r requirements.txt
    ```
- Create config file in :
    ```
    src/main/config.py
    ``` 
- Fill config file.
- Cd demodayreporttool in command line for install setup:
    ```sh
    pip install .
    ```

# Config file :
* File must be format __Python__ 
* File have information for access for your board
* For access your config.py __must be__ imported in your src/main/config.py
* You need get __key__, __token__ and __id list__ for fill space.
```Python
class TrelloApi:
    key = "keyTrelloAPI"
    token = "tokenTrelloAPI"

class ListID:
    todo_id = "Listid"
    in_progress_id = "Listid"
    code_review_id = "Listid"
    in_test_id = "Listid"
    release_id = "Listid"
    done_id = "Listid"

class BoardID:
    board_id = "Boardid"
```

# Setup.py install :
* cd your_project in command line and after:
```  
pip install .
```

## Commands :
* __generate_report__ - create presentation.

## History of commits :
* [Commits](https://github.com/vladislav-lopa/demodayreporttool/tree/feature/clone-demo-day-report-tool-from-bitbucket/History_of_commits_from_bitbucket.png)

## Changelog :
* [Changelog](https://github.com/vladislav-lopa/demodayreporttool/tree/feature/clone-demo-day-report-tool-from-bitbucket/CHANGELOG.md)
