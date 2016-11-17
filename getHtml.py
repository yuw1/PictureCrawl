#encoding=utf-8
import urllib


class getHtml:
    def __init__(self,url):
        self.url=url
    def getHtml(self):
        try:
            page = urllib.urlopen(self.url)
            html = page.read()
            return html
        except Exception, e:
            print "获取网页失败"
            return None