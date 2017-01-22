#Config the request header, could include the user-agent, accept-encoding and other info


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '\
'Chrome/55.0.2883.75 Safari/537.36"
ACCEPT_ENCODING = "gzip, deflate, sdch"
ACCEPT_LANGUAGE = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
#if need
# CONNECTION = "keep-alive"

HEADER = {'User-Agent': USER_AGENT, "Accept-Encoding": ACCEPT_ENCODING, '\
'"Accept-Language": ACCEPT_LANGUAGE}
