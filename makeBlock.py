import json

import wmp
import coupang


def getTop3(product, user):

    json_data = open('test.json',encoding='UTF8').read()

    json_t = json.loads(json_data)
    # print(json_t)

    #
    # print(coupang.coupang("휴지"))
    # print("-----------------------------------")
    # print(wmp.wmp_search("휴지"))

    json_t[0]['text']['text'] = json_t[0]['text']['text'].format(user)

    coupangList = coupang.coupang(product)
    wmpList = wmp.wmp_search(product)


    # 쿠팡 3,4,5 / 위메프 8,9,10

    # 쿠팡 정보 입력  "상품링크","상품명","평점","가격"
    json_t[3]['text']['text'] = json_t[3]['text']['text'].format(coupangList[0][0], coupangList[0][1], coupangList[0][3], coupangList[0][2])
    json_t[4]['text']['text'] = json_t[4]['text']['text'].format(coupangList[1][0], coupangList[1][1], coupangList[1][3], coupangList[1][2])
    json_t[5]['text']['text'] = json_t[5]['text']['text'].format(coupangList[2][0], coupangList[2][1], coupangList[2][3], coupangList[2][2])

    #위메프 정보 입력  "상품링크","상품명","평점","가격"
    json_t[8]['text']['text'] = json_t[8]['text']['text'].format(wmpList[0][0], wmpList[0][1], wmpList[0][3],wmpList[0][2])
    json_t[9]['text']['text'] = json_t[9]['text']['text'].format(wmpList[1][0], wmpList[1][1], wmpList[1][3],wmpList[1][2])
    json_t[10]['text']['text'] = json_t[10]['text']['text'].format(wmpList[2][0], wmpList[2][1], wmpList[2][3],wmpList[2][2])


    #이미지 주소 입력
    json_t[3]['accessory']['image_url'] = json_t[3]['accessory']['image_url'].format(coupangList[0][-1])
    json_t[4]['accessory']['image_url'] = json_t[4]['accessory']['image_url'].format(coupangList[1][-1])
    json_t[5]['accessory']['image_url'] = json_t[5]['accessory']['image_url'].format(coupangList[2][-1])

    json_t[8]['accessory']['image_url'] = json_t[8]['accessory']['image_url'].format(wmpList[0][-1])
    json_t[9]['accessory']['image_url'] = json_t[9]['accessory']['image_url'].format(wmpList[1][-1])
    json_t[10]['accessory']['image_url'] = json_t[10]['accessory']['image_url'].format(wmpList[2][-1])


    #상품 이름 입력
    json_t[3]['accessory']['alt_text'] = json_t[3]['accessory']['alt_text'].format(coupangList[0][1])
    json_t[4]['accessory']['alt_text'] = json_t[4]['accessory']['alt_text'].format(coupangList[1][1])
    json_t[5]['accessory']['alt_text'] = json_t[5]['accessory']['alt_text'].format(coupangList[2][1])

    json_t[8]['accessory']['alt_text'] = json_t[8]['accessory']['alt_text'].format(wmpList[0][1])
    json_t[9]['accessory']['alt_text'] = json_t[9]['accessory']['alt_text'].format(wmpList[1][1])
    json_t[10]['accessory']['alt_text'] = json_t[10]['accessory']['alt_text'].format(wmpList[2][1])

    return json_t

    # {
    #     "type": "section",
    #     "text": {
    #         "type": "mrkdwn",
    #         "text": "> *<{0}|{1}>* \n 평점 : {2}  \n 가격 : {3} 원 ~"
    #     },
    #     "accessory": {
    #         "type": "image",
    #         "image_url": "https://image.wemakeprice.com/deal/4/716/4527164/bdeb9de4c1bd94f0cbd270910ff608c4edd44cc5.jpg?modify=D_1562819640",
    #         "alt_text": "[상품명]"
    #     }
    # }