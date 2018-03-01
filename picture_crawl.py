import queue
import threading

from Html import Html
from Image import Image
from Url import Url


def getHtml(urlNum, allUrlList, urlImgQueue, urlQueue):
    while (urlNum < 20 and urlQueue.not_empty):
        url = urlQueue.get()

        thisHtml = Html(url)
        html = thisHtml.getHtml()

        if (html != None):
            thisUrl = Url(html, allUrlList, urlQueue, urlImgQueue, urlNum)
            allUrlList, urlQueue, urlImgQueue, urlNum = thisUrl.getUrl()


def getImg(allImgList, imgNum):
    localImgNum = 0
    while (localImgNum < 10 and urlImgQueue.not_empty):
        url = urlImgQueue.get()

        thisHtml = Html(url)
        html = thisHtml.getHtml()

        if (html != None):
            thisImg = Image(html, localImgNum, allImgList, imgNum)
            localImgNum, allImgList = thisImg.getImg()


if __name__ == "__main__":
    urlQueue = queue.Queue()
    urlImgQueue = queue.Queue()
    allUrlList = []
    allImgList = []

    urlQueue.put('http://www.fzlu.net/fengjingtupian/20158799.html')
    urlImgQueue.put('http://www.fzlu.net/fengjingtupian/20158799.html')
    allUrlList.append('http://www.fzlu.net/fengjingtupian/20158799.html')

    urlNum = 0
    imgNum = 0

    getHtml(urlNum, allUrlList, urlImgQueue, urlQueue)

    threadingList = []
    for i in range(10):
        t = threading.Thread(target=getImg, name='LoopThread', args=(allImgList, i * 10))
        t.start()
        threadingList.append(t)
    for t in threadingList:
        t.join()
