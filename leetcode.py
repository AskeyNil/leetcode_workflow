# coding=utf-8
import requests
import time
from alfred_api import *

url = "https://leetcode-cn.com/graphql"
today_request = {
    "operationName": "questionOfToday",
    "variables": {},
    "query": "query questionOfToday { todayRecord { question { questionFrontendId questionTitleSlug translatedTitle } } }"
}
data = requests.post(url, json=today_request).json()
question = data["data"]["todayRecord"][0]["question"]
today_id = question["questionFrontendId"]
today_slug = question["questionTitleSlug"] 
today_title = question["translatedTitle"]
today_time = time.strftime("%Y-%m-%d", time.localtime())

copy_title = u"{}.{}".format(today_id, today_title)
cmd_title = u"cmd + c 复制题目：{}".format(copy_title)
m = Mod(cmd_title, "", Mod.Type.CMD)
copy_text = Text(copy_title, Text.Type.COPY)
large_text = Text(copy_title, Text.Type.LARGETYPE)

title = u"{}: {}".format(today_time, copy_title)
subtitle = "https://leetcode-cn.com/problems/{}/".format(today_slug)
item = Item(title, subtitle, arg=today_slug, mods=[m], text=[copy_text, large_text])
export([item])
