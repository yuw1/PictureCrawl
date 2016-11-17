import Queue

from getHtml import getHtml
from getImg import getImg
from getUrl import getUrl

urlQueue=Queue.Queue()
urlImgQueue=Queue.Queue()
allUrlList=[]
allImgList=[]

urlQueue.put('http://www.fzlu.com/meinvtupian/20154371.html')
urlImgQueue.put('http://www.fzlu.com/meinvtupian/20154371.html')
allUrlList.append('http://www.fzlu.com/meinvtupian/20154371.html')

urlNum = 0
imgNum = 0

while(urlNum<200 and urlQueue.not_empty):
    url=urlQueue.get()

    thisHtml = getHtml(url)
    html = thisHtml.getHtml()

    if(html!=None):
        thisUrl=getUrl(html,allUrlList,urlQueue,urlImgQueue,urlNum)
        allUrlList,urlQueue,urlImgQueue,urlNum=thisUrl.getUrl()

while(imgNum<1000 and urlImgQueue.not_empty):
    url = urlImgQueue.get()

    thisHtml = getHtml(url)
    html = thisHtml.getHtml()

    if (html != None):
        thisImg = getImg(html, imgNum, allImgList)
        imgNum, allImgList = thisImg.getImg()