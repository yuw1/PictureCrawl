# encoding=utf-8
from urllib import request


class Html:
    def __init__(self, url):
        self.url = url

    def getHtml(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
        headers = {'User-Agent': user_agent}
        req = request.Request(url=self.url, headers=headers)
        try:
            page = request.urlopen(req)
            html = page.read()
            return html
        except Exception as e:
            print("获取网页失败")
            return None
