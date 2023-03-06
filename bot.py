from utils import *
from variables import *


class Bot ():  # using Undetected Chrome Web driver

    def __init__(self) -> None:
        self.running_status = False

    def start(self, headless=False):
        print('...')
        options = uc.ChromeOptions()
        # options.add_argument('--no-sandbox')
        # options.add_argument('--blink-settings=imagesEnabled=false')

        options.add_argument('--disable-gpu')
        if headless:
            options.headless = True
            options.add_argument('--headless')

        # options = {
        #     'proxy': {
        #         'http': 'socks5://user:pass@192.168.10.100:8888',
        #         'https': 'socks5://user:pass@192.168.10.100:8888',
        #         'no_proxy': 'localhost,127.0.0.1'
        #     }
        # }

        self.driver = uc.Chrome(options=options)

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

    def search_on_google(self, search_string):
        self.goto("https://www.google.com")
        self.wait_xpath("//input[@title='Search']")
        search = self.driver.find_element(
            By.XPATH, "//input[@title='Search']")
        search.send_keys(search_string)
        search.send_keys(Keys.ENTER)

    def click_on_google_ads_website(self, website):
        # //div[count(span)=3 and span[1][text()='Ad']]
        # xpath = "//div[count(span)=3 and span[1][text()='Ad']]"
        xpath = "//*[@data-dtld]"

        self.wait_xpath(xpath)
        adds = self.driver.find_elements(
            By.XPATH, xpath)
        print(f'{len(adds)}=')
        for div in adds:
            text = div.text
            print(text)
            if website in div.text:
                webdriver.ActionChains(self.driver)\
                    .move_to_element(div).click().perform()
                print('clicked')
                return
            # text = div.text
            # print(text)
            # text = div.
            # print(text)
        # return adds

    def click_on_google_site(self, website):
        # //cite
        xpath = "//cite"

        self.wait_xpath(xpath)
        adds = self.driver.find_elements(
            By.XPATH, xpath)
        print(f'{len(adds)}=')
        for div in adds:
            text = div.text
            print(text)
            if website in div.text:
                webdriver.ActionChains(self.driver)\
                    .move_to_element(div).click().perform()
                print('clicked')
                return

    def change_ip(self, proxy):
        # Change the proxy
        #  {
        #     'http': 'http://192.168.10.100:8888',
        #     'https': 'https://192.168.10.100:8888',
        #     'no_proxy': 'localhost,127.0.0.1'
        # }
        self.driver.proxy = proxy

        sleep(2)

    def what_is_my_ip(self):
        try:
            self.goto("https://api.myip.com/")
            self.wait_xpath('//body')
            return self.driver.find_element(By.XPATH, '//body').text
        except Exception as e:
            print("Unable to fetch IP,Error: ", e)

    def quit(self):
        self.driver.quit()

    def __del__(self):
        self.running_status = False
        self = None
