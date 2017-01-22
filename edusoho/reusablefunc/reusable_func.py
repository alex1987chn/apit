import io
import json
import sys

import requests
from lxml import etree

import agent_setting

# AGENT = importlib.import_module('agent_setting')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030') #改变标准输出的默认编码


def get_csrftoken_cookie(web_url):
    with open('./data.json', 'r') as f:
        data = json.load(f)

    header = agent_setting.HEADER
    response_page = requests.get(url=data[web_url], headers=header)
    cookie = response_page.cookies
    parse_page = etree.HTML(text=response_page.text)
    csrf_token = parse_page.xpath('//meta[@name="csrf-token"]/@content')[0]
    collections = [csrf_token, cookie]
    return collections
