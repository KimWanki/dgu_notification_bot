# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# URL = 'http://deal.11st.co.kr/html/nc/deal/main.html'
# DRIVER_PATH = './crawler/driver/chromedriver 4'
#
# chrome_options = Options()
# # TODO : WebDriver를 Browser 없이 실행하는 옵션. : --headless
# chrome_options.add_argument('--headless')
# # TODO :  ln: Chroem Browser의 로그 레벨을 낮추는 옵션.
# chrome_options.add_argument( '--log-level=3' )
# # TODO : ln: 로그를 남기지 않는 옵션.
# #  * chromedriver의 버전에 따라 적용이 안될 수도 있지만, 로그 레벨만 낮춰도 로그가 출력되지 않음.
# chrome_options.add_argument( '--disable-logging' )
# chrome_options.add_argument( '--no-sandbox' )
# chrome_options.add_argument( '--disable-gpu' )
#
# driver = webdriver.Chrome( executable_path=DRIVER_PATH, chrome_options=chrome_options )
#
# driver.get(URL)
#
# # print(driver.page_source)
# # @COPY SELECT 에 대한 결과 값 :  #emergencyPrd > div > ul
#
# # elements = driver.find_elements_by_css_selector('#emergencyPrd > div > ul > li')
#
# elements = driver.find_elements_by_xpath('//*[@id="emergencyPrd"]/div/ul/li[position()<=3]')
# print('상품 개수: {}'.format(len(elements)))
# print(elements[0].get_attribute('innerHTML'))
# for el in elements:
#
#
#     el_title = el.find_element_by_xpath('div/a/div[3]/p/span')
#     el_price = el.find_element_by_xpath('div/a/div[3]/div/span[2]/strong')
#
#
#     # el_title = el.find_element_by_css_selector('div > a > div.prd_info > p > span.fs_16')
#     # el_price = el.find_element_by_css_selector('div > a > div.prd_info > div > span.price_detail > strong')
#
#     tagName = el_title.tag_name
#     className = el_title.get_attribute('class')
#     title = el_title.text
#     price = el_price.text
#
#     print('=' * 50)
#     print('tagName: {}'.format(tagName))
#     print('className: {}'.format(className))
#     print('title: {}'.format(title))
#     print('price: {}'.format(price))
#
#

from crawler import SeleniumRequest
from crawler.parser import st11_parser, tmon_parser, wemap_parser
from pprint import pprint


from crawler import SeleniumRequest
from crawler.parser import st11_parser, tmon_parser, wemap_parser, dongguk_scholar_parser, dongguk_normal_parser
from pprint import pprint

targets = {
    "dongguk_scholar": {
        "url": 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3638&id=kr_010801000000'
        , "parser": "dongguk_scholar_parser"
        , "data": None
    }
    ,
    "dongguk_normal": {
        "url": 'https://www.dongguk.edu/mbs/kr/jsp/board/list.jsp?boardId=3646&id=kr_010802000000'
        , "parser": "dongguk_normal_parser"
        , "data": None
    }

}

def run(target):
    request = SeleniumRequest(driver_path='./crawler/driver/chromedriver 4')

    info = targets[target]

    url = info['url']
    callback = eval(info["parser"])

    data = request.get(url, callback=callback)

    return data

if __name__ == '__main__':
    request = SeleniumRequest(driver_path='./crawler/driver/chromedriver 4')

    for key in targets.keys():
        info = targets[key]

        url = info['url']
        callback = eval(info["parser"])

        data = request.get(url, callback=callback)
        targets[key]["data"] = data

    pprint(targets)

