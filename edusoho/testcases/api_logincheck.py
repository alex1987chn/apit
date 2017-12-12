# encoding=utf-8
# python3.6.3
import json
import assertpy
import requests
from lxml import etree

import agent_setting
from reusablefunc import reusable_func

# from lxml import etree
HEADER = agent_setting.HEADER
with open('.\edusoho\data.json', 'r') as f:
    DATA = json.load(f)

 # get cookie&token in collection
COLLECTION = reusable_func.get_csrftoken_cookie('try3_login_url')
CSRF_TOKEN = COLLECTION[0]  # get csrf_token
COOKIE = COLLECTION[1]  # get cookie

DATA['body']['_csrf_token'] = CSRF_TOKEN
DATA['body']['_target_path'] = 'http://try3.edusoho.cn/'

# get the response page
PAGE = requests.post(url=DATA['try3_login_check'], data=DATA['body'],
                     headers=HEADER, cookies=COOKIE)
# Assertion
assertpy.assert_that(PAGE.status_code).is_equal_to(200)
