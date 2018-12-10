import requests
from bs4 import BeautifulSoup
from lxml import html
from csv import DictReader

url = 'https://www.yemeksepeti.com/istanbul/akatlar'
def creating_soup(url):
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    content_div = soup('div', attrs={'class': 'ys-reslist'})
    return content_div

def working_on_soup(content):
    results = {}
    for items in content:
        item = []
        some_items = items.find('div', attrs={'class': 'ys-reslist-items'})
        not_promoted_items = some_items.find_all('div', attrs={'class': 'ys-item'})
        for data in not_promoted_items:
            item_data = data.find('a', attrs={'class': 'restaurantName withTooltip'})
            if item_data:
                item.append(item_data.text.strip())
            else:
                item.append('N/a')
'''
    for other_items in content:
        promoted_item = []
        promoted_items = items.find('div', attrs={'class': 'ys-promoted-reslist-items'}).find_all('div', attrs={'class': 'ys-item'})
        for promored_data in promoted_items:
            promoted_item_data = promored_data.find('a', attrs={'class': 'restaurantName withTooltip'})
            if promoted_item_data:
                promoted_item.append(promoted_item_data.text.strip())
            else:
                promoted_item.append('N/a')

 
 
    results['rest-url'] = url
    results['promoted-items'] = promoted_item
    results['not-promoted-items'] = item
    return print(results)
'''


working_on_soup(creating_soup(url))

'''
    for promoted_items in promoted_divs:
        item = {}
        real_item = promoted_items.find('a', attrs={'class': 'restaurantName withTooltip'})
        if real_item:
            item['promoted-items'] = real_item.text
        else:
            item['promoted-items'] = 'N/A'
    results.append(item)
    simple_divs = content.find('div', attrs={'class':'ys-reslist-items'})
    print(results)
'''

'''
def parsing_soup(content):
    promoted_data_div = content.find('div', attrs={'class': 'ys-promoted-reslist-items '})
    promoted_list = promoted_data_div.find_all('a', attrs={'class': 'restaurantName withTooltip'})
    local_results = []
    local_results.append(url)
    for names in promoted_list:
        names.find('a', attrs={'class': 'restaurantName withTooltip'})
        local_results.append(names.text.strip())
        return results.append(local_results)
    simple_data_div = content.find('div', attrs={'class': 'ys-reslist-items'})
    simple_list = simple_data_div.find_all('div', attrs={'class': ''})
    return print(results)
parsing_soup(creating_soup(url))

print(results)
'''