from utils import *


class Bot ():  # using Undetected Chrome Web driver

    def __init__(self) -> None:
        self.running_status = False

    def start(self, headless=False):
        print('...')
        options = uc.ChromeOptions()

        if headless:
            options.headless = True
            options.add_argument('--headless')

        self.driver = uc.Chrome(options=options, seleniumwire_options={})

        self.wait = WebDriverWait(self.driver, 60)
        self.running_status = True

    def stop(self):
        if self.running_status:
            self.driver.quit()
            self.running_status = False

    def goto(self, url):
        self.driver.get(url)
        sleep(2)

    # wait for methods
    def wait_css_selector(self, code):
        self.wait.until(
            ExpectedConditions.presence_of_element_located(
                (By.CSS_SELECTOR, code))
        )

    def wait_css_selectorTest(self, code):
        self.wait.until(
            ExpectedConditions.elementToBeClickable((By.CSS_SELECTOR, code))
        )

    def wait_xpath(self, code):
        self.wait.until(
            ExpectedConditions.presence_of_element_located((By.XPATH, code)))

    def check_exists_by_tagname(self, tagname):
        try:
            self.driver.find_element(By.TAG_NAME, tagname)
        except NoSuchElementException:
            return False
        return True

    def start_browser(self):
        self.stop()
        self.start()
        self.goto("https://www.google.com")

    def quit(self):
        self.driver.quit()

    def __del__(self):
        self.running_status = False
        self = None
