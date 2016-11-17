import re

class getUrl():
    def __init__(self,html,allUrlList,urlQueue,urlImgQueue,urlNum):
        self.html=html
        self.allUrlList=allUrlList
        self.urlQueue=urlQueue
        self.urlImgQueue=urlImgQueue
        self.urlNum=urlNum
    def getUrl(self):
        reg = r"href='(/meinvtupian.+?\html|/mingxingtupian.+?\html)'"
        urlre = re.compile(reg)
        urllist = re.findall(urlre, self.html)
        if(urllist!=None):
            for i in range(len(urllist)):
                urllist[i]='http://www.fzlu.com' + urllist[i]
            print urllist
            print self.allUrlList
            newAllUrlList=list(set(urllist+self.allUrlList))
            urllist=list(set(newAllUrlList)-set(self.allUrlList))
            for url in urllist:
                self.allUrlList.append(url)
                self.urlQueue.put(url)
                self.urlImgQueue.put(url)
            self.urlNum=self.urlNum + len(urllist)
            print self.urlNum

        return self.allUrlList,self.urlQueue,self.urlImgQueue,self.urlNum

