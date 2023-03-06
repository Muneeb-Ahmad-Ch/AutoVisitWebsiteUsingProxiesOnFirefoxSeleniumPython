from bot import *

if __name__ == '__main__':
    KEYWORD = 'python'
    ##
    bot = Bot()
    bot.start_browser()
    bot.wait_xpath("//input[@title='Search']")
    search = bot.driver.find_element(
        By.XPATH, "//input[@title='Search']")
    search.send_keys(KEYWORD)
    search.send_keys(Keys.ENTER)
