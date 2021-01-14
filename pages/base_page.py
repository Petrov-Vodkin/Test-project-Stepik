class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitlywait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        self.browser.find_element(how, what)
