## Frontend test automation - Page Object framework

> Python | Pytest | Selenium | Allure

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies
```bash
pip install -r requirements.txt 
```
2. [Downloading](https://github.com/allure-framework/allure2/releases/tag/2.13.10)
and [installing](https://docs.qameta.io/allure/#_get_started) **Allure** commandline application suitable for your environment
## Usage
Run `Chrome` browser tests
```bash
pytest -v
pytest -v --tb=line
pytest -v -s --tb=line --language=en
pytest -v --tb=line --language=en -m need_review
```
Run `Firefox` browser tests
```bash
pytest -v -s --tb=line --browser_name=firefox --language=en
```
Run tests with execution reports `Allure`
```bash
pytest --alluredir name_dir_allure_result name_test
```
```bash
allure serve name_dir_allure_result # result of test  
```

## Related links
[Stepik course link](https://stepik.org/course/575/) |
[Certificate link](https://stepik.org/cert/230000) |
[Web app link](http://selenium1py.pythonanywhere.com/) | 
[Allure link](http://allure.qatools.ru/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
