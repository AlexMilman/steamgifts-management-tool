from BusinessLogic.ScrapingUtils import SteamGiftsScrapingUtils
from BusinessLogic.Utils import StringUtils, WebUtils

# All scraping implementations for SGtools
# Copyright (C) 2017  Alex Milman

sgtools_check_nonactivated_link = 'http://www.sgtools.info/nonactivated/'
sgtools_check_multiple_wins_link = 'http://www.sgtools.info/multiple/'
sgtools_check_sent_link = 'http://www.sgtools.info/sent/'
sgtools_check_won_link = 'http://www.sgtools.info/won/'


def check_level(user, level):
    user_html_content = WebUtils.get_html_page(SteamGiftsScrapingUtils.get_user_link(user))
    user_level_item = WebUtils.get_item_by_xpath(user_html_content, u'.//div[@class="featured__table__row__right"]/span/@data-ui-tooltip')
    user_level = user_level_item.split('name" : "')[2].split('", "color')[0]
    return StringUtils.normalize_float(user_level) < level


def check_real_cv_value(user):
    sent_html_content = WebUtils.get_html_page(sgtools_check_sent_link + user)
    sent_value = WebUtils.get_item_by_xpath(sent_html_content, u'.//div[@class="total"]/h1/text()').replace('$', '')
    won_html_content = WebUtils.get_html_page(sgtools_check_won_link + user)
    won_value = WebUtils.get_item_by_xpath(won_html_content, u'.//div[@class="total"]/h1/text()').replace('$', '')
    return StringUtils.normalize_float(won_value) > StringUtils.normalize_float(sent_value)


def check_multiple_wins(user):
    return WebUtils.get_page_content(sgtools_check_multiple_wins_link + user).find(' has no multiple wins for the same game!') == -1


def check_nonactivated(user):
    nonactivated_page_content = WebUtils.get_page_content(sgtools_check_nonactivated_link + user)
    return nonactivated_page_content.find(' has activated all his/her games!') == -1 and nonactivated_page_content.find('Games wins not activated') != -1
