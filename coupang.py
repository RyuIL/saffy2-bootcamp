import re
import requests
from bs4 import BeautifulSoup

from operator import itemgetter

def coupang(product):
    # 크롤링 함수 구현하기
    # url = "https://music.bugs.co.kr/chart"
    # source_code = urllib.request.urlopen(url).read()
    # soup = BeautifulSoup(source_code, "html.parser")
    url = 'https://www.coupang.com/np/search?component=&q='+product+'&channel=user'

    request_header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'      
    }
    # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
    req = requests.get(url, headers = request_header)
    html = req.text    
    soup = BeautifulSoup(html, 'html.parser')

    price_list = []
    coupang_dict = {}
    coupang_list = []
    
    i = 0
    for searchItem in soup.find_all("li", class_="search-product"):
        price = searchItem.find("strong", class_="price-value")
        name = searchItem.find("div", class_="name")
        isHaveRating = False
        if(searchItem.find("em", class_="rating")):
            rating = searchItem.find("em", class_="rating").text
            isHaveRating = True
        else : rating = "0"
        rating_total_count = searchItem.find("span", class_="rating-total-count")
        # search_product_wrap_img = searchItem.find("img", class_="search-product-wrap-img")
        search_product_wrap_img = searchItem.select("dt.image > img.search-product-wrap-img")
        search_product_link = searchItem.find('a', class_="search-product-link")['href']
        search_product_link = "https://www.coupang.com"+search_product_link
        print(name.text)
        print(price.text)
        print(rating)
        if isHaveRating:
            rating_count = rating_total_count.text.replace("(","").replace(")","")
        else : rating_count = "0"
        # print(rating_count)
        # print("http:"+search_product_wrap_img['src'])

        coupang_list.append([search_product_link, name.text, int(price.text.replace(",","")), float(rating), int(rating_count)])

        if(not "gif" in search_product_wrap_img[0]['src']):
            # print(search_product_wrap_img[0]['src'])
            coupang_list[i].append(search_product_wrap_img[0]['src'])
        else : 
            # print(search_product_wrap_img[0]['data-img-src'])
            coupang_list[i].append(search_product_wrap_img[0]['data-img-src'])

        # print(coupang_list)
        i+=1
        if i==20 :
            break

        # for item in coupang_list:
        #     print(item)
        
        

        # recommend = []
        # temp2 = sorted(coupang_list, key = itemgetter(3,4), reverse=True)

        # temp = coupang_list.sort(key=itemgetter(2), reverse=True)

        # for item in temp2:
        #     print(item[2])
    # print(i)

    result_str = ""
    ix = 1
    sortedList = sorted(coupang_list, key=lambda x : x[3], reverse=True)[:3]

    # for item in sorted(coupang_list, key=lambda x: x[2], reverse=True):
    #     result_str += str(ix) + "." + item[0] + " / 가격 : " + str(item[1]) + "   사러 가기 : " + item[4] + "\n"
    #     ix += 1


    return sortedList
