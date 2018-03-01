#encoding=utf-8
import re
import threading
from urllib import request


class Image:
    def __init__(self,html,num,allImgList,baseImgNum):
        self.num=num
        self.html=html
        self.allImgList=allImgList
        self.html = self.html.decode('gbk')
        self.baseImgNum = baseImgNum
    def getImg(self):
        try:
            reg = r'src="(.+?\.jpg)"'
            imglist = re.findall(reg, self.html)
            if (len(imglist)):
                for i in range(len(imglist)):
                    imglist[i]='http://www.fzlu.com' +imglist[i]
                for imgurl in imglist:
                    try:

                        request.urlretrieve(imgurl, 'E:/photo/%d.jpg' % (self.num + self.baseImgNum))
                        print('已保存第%d张图片' % (self.num + self.baseImgNum))
                        print(threading.current_thread())
                        self.allImgList.append(imgurl)
                        if self.num == 10 :
                            break
                    except Exception as e:
                        print(e.args)
                request.urlcleanup()

        except Exception as e:
            print("正则表达式异常")
        return self.num, self.allImgList