from bot import *

if __name__ == '__main__':
    KEYWORD = 'python'
    ##
    bot = Bot()
    bot.start_browser()
    bot.change_ip('139.99.135.214', '80')
    print(f'{bot.what_is_my_ip()=}')
    # bot.search_on_google(KEYWORD)

    input('Press any key to quit...')
    bot.quit()
