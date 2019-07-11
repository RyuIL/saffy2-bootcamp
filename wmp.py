import requests
import urllib.request

from bs4 import BeautifulSoup
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

SLACK_TOKEN = 'xoxb-685325156311-691504642295-0IicknNu78Wm7bOWAYNoVVHm'
SLACK_SIGNING_SECRET = '00d36252a2c5491e3730360c567d154a'


app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


def wmp_search(text):

    url = 'https://search.wemakeprice.com/search?search_keyword=' + text.split()[1]
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('div.box_listwrap.tab_cont > div > a')
    output = []

    for item in items[:50] :
        link = "http:" + item["href"]
        title = item.select('div > img')[0]['alt']
        price = item.find('em', class_='num').get_text()
        rank = item.find('i').get_text()
        howMany = item.find('span', class_='num').get_text()
        img_src = item.select('div > img')[0]['data-lazy-src']
        output.append([link, title, int(price.replace(',','')), float(rank.split()[1]), int(howMany.replace(',','')), img_src])

    print(output)
    tem = ''
    # print("추천아이템은 " + sorted(output, key=lambda x:x[3], reverse = True)[0] + "입니다")

    return tem





@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    # 슬랙 챗봇이 대답합니다.
    text = event_data["event"]["text"]
    message = wmp_search(text)
    slack_web_client.chat_postMessage(
        channel=event_data["event"]["channel"],
        text=message
    )


# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=4040)
