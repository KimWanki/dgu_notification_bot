def st11_parser(response=None):
    datas = list()

    elements = response.find_elements_by_xpath('//*[@id="emergencyPrd"]/div/ul/li[position()<=3]')

    for idx, el in enumerate(elements):
        el_title = el.find_element_by_xpath('div/a/div[3]/p/span')
        el_price = el.find_element_by_xpath('div/a/div[3]/div/span[2]/strong')
        el_link = el.find_element_by_xpath('div/a')

        title = el_title.text.strip()
        price = el_price.text.replace(',', '').strip()
        link = el_link.get_attribute('href')

        data = {
            "no": idx + 1
            , "title": title
            , "price": price
            , "link": link
        }

        datas.append(data)

    return datas


def tmon_parser(response=None):
    datas = list()

    elements = response.find_elements_by_xpath('//*[@id="_dealList"]/li[position()<=3]')
    for idx, el in enumerate(elements):
        el_title = el.find_element_by_xpath('a/div/div[3]/p[2]')
        print(el_title.text.strip())
        el_price = el.find_element_by_xpath('a/div/div[3]/div[2]/span[1]/span/i')
        el_link = el.find_element_by_xpath('a')

        title = el_title.text.strip()
        price = el_price.text.replace(',', '').strip()
        link = el_link.get_attribute('href')

        data = {
            "no": idx + 1
            , "title": title
            , "price": price
            , "link": link
        }
        datas.append(data)

    return datas


def wemap_parser(response=None):
    datas = list()
    elements = response.find_elements_by_xpath('//*[@id="_contents"]/div/div[2]/div[3]/div[3]/div/a[position()<=3]')
    for idx, el in enumerate(elements):
        el_title = el.find_element_by_xpath('div/div[2]/div[1]/p')
        el_price = el.find_element_by_xpath('div/div[2]/div[1]/div/div[2]/strong/em')
        el_link = el

        title = el_title.text.strip()
        price = el_price.text.replace(',', '').strip()
        link = el_link.get_attribute('href')

        data = {
            "no": idx + 1
            , "title": title
            , "price": price
            , "link": link
        }
        datas.append(data)

    return datas


def dongguk_scholar_parser(response=None):
    datas = list()
    elements = response.find_elements_by_xpath('//*[@id="board_list"]/tbody/tr[10<position() and position()<15]')
    for idx, el in enumerate(elements):
        # // *[ @ id = "board_list"] / tbody / tr[11] / td[2] / img
        # el_num = el.find_element_by_xpath('td[1]')
        el_title = el.find_element_by_xpath('td[2]/a')
        el_date = el.find_element_by_xpath('td[4]')
        el_link = el_title
        # el_num = el_num.text.strip()
        title = el_title.text.strip()
        date = el_date.text.replace(',', '').strip()

        link = el_link.get_attribute('href')
        data = {
            "no": idx + 1
            , "title": title
            , "date": date
            , "link": link
        }

        datas.append(data)

    return datas

def dongguk_normal_parser(response=None):
    datas = list()
    elements = response.find_elements_by_xpath('//*[@id="board_list"]/tbody/tr[10<position() and position()<15]')
    for idx, el in enumerate(elements):
        # // *[ @ id = "board_list"] / tbody / tr[11] / td[2] / img
        # el_num = el.find_element_by_xpath('td[1]')
        el_title = el.find_element_by_xpath('td[2]/a')
        el_date = el.find_element_by_xpath('td[4]')
        el_link = el_title
        # el_num = el_num.text.strip()
        title = el_title.text.strip()
        date = el_date.text.replace(',', '').strip()

        link = el_link.get_attribute('href')
        data = {
            "no": idx + 1
            , "title": title
            , "date": date
            , "link": link
        }

        datas.append(data)

    return datas

