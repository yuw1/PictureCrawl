#encoding=utf-8
from urllib import request


class Html:
    def __init__(self,url):
        self.url=url
    def getHtml(self):
        try:
            page = request.urlopen(self.url)
            html = page.read()
            return html
        except Exception as e:
            print("获取网页失败")
            return None