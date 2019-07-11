import requests
from bs4 import BeautifulSoup



def wmp_search(text):

    url = 'https://search.wemakeprice.com/search?search_keyword=' + text
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('div.box_listwrap.tab_cont > div > a')
    output = []

    for item in items[:10] :
        link = "http:" + item["href"]
        title = item.select('div > img')[0]['alt']
        price = item.find('em', class_='num').get_text()
        rank = item.find('i').get_text()
        howMany = item.find('span', class_='num').get_text()
        img_src = item.select('div > img')[0]['data-lazy-src']
        output.append([link, title, int(price.replace(',','')), float(rank.split()[1]), int(howMany.replace(',','')), img_src])

    # print(output)

    # tem = output
    # print("추천아이템은 " + sorted(output, key=lambda x:x[3], reverse = True)[0] + "입니다")

    result = sorted(output, key=lambda x:x[3], reverse = True)[:3]

    return result
