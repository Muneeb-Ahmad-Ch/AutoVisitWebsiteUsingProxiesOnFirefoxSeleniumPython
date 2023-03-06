from bot import *

if __name__ == '__main__':
    KEYWORD = 'master paints'
    WEBSITE_LINK = 'masterpaints.com'
    ##
    bot = Bot()
    bot.start_browser()
    # bot.change_ip(proxy=OPTIONS['proxy'])
    # print(f'{bot.what_is_my_ip()=}')
    try:
        bot.search_on_google(KEYWORD)
        # to click website of ads
        # bot.click_on_google_ads_website(WEBSITE_LINK)
        # to click on normal website link
        bot.click_on_google_site(WEBSITE_LINK)
    except:
        pass
    input('Press any key to quit...')
    bot.quit()
