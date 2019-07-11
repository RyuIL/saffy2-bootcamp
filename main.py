from flask import Flask
from slack import WebClient
from slack.web.classes import extract_json
from slack.web.classes.blocks import *
from slackeventsapi import SlackEventAdapter

import makeBlock

SLACK_TOKEN = 'xoxb-685325156311-691504642295-2rHbrKkK5ja0Qc4jKFLoQbZU'
SLACK_SIGNING_SECRET = '00d36252a2c5491e3730360c567d154a'


app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


# @slack_events_adaptor.on("app_mention")
# def app_mentioned(event_data):
#     # 슬랙 챗봇이 대답합니다.
#     text = event_data["event"]["text"]
#     # message = wmp_search(text)
#     message = "hahahahaha"
#     slack_web_client.chat_postMessage(
#         channel=event_data["event"]["channel"],
#         text=message
#     )


# 블럭 생성 테스트
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    # 슬랙 챗봇이 대답합니다.
    #
    # block1 = ImageBlock(image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUwoh2AA9A1jkEL8W2U5be86T0fcyUqqFGcU5CTBxDDfnme5yKMw", alt_text="이미지가안뜰때보이는문구")
    # block2 = SectionBlock( text={ "type":"mrkdwn", "text":"Danny Torrence left the following review for your property:" })
    # block3 = SectionBlock(
    #     fields=["text1", "text2"]
    # )
    # json_data = open('test.json').read()
    # print(json_data)
    # block4 = Block({"type": "section","text": {"type": "mrkdwn","text": "Danny Torrence left the following review for your property:"}})
    # json1 = [{"type": "section","text": {"type": "mrkdwn","text": "Danny Torrence left the following review for your property:"}}]
    # print(type(json1[0]))
    # my_blocks = [block1, block2, block3]

    text = event_data["event"]["text"]

    block = makeBlock.getTop3(text.split()[1])

    slack_web_client.chat_postMessage(
        channel= event_data["event"]["channel"],
        blocks = block
    )

# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=4040)
