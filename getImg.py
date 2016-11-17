#encoding=utf-8
import re
import urllib


class getImg:
    def __init__(self,html,num,allImgList):
        self.num=num
        self.html=html
        self.allImgList=allImgList
    def getImg(self):
        try:
            reg = r'src="(.+?\.jpg)"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, self.html)
            print imglist
            if (len(imglist)):
                for i in range(len(imglist)):
                    imglist[i]='http://www.fzlu.com' +imglist[i]
                # for imgurl in imglist:
                #     for allImgUrl in self.allImgList:
                #         if (imgurl == allImgUrl):
                #             imglist.remove(imgurl)
                print imglist
                for imgurl in imglist:
                    try:
                        urllib.urlretrieve(imgurl, 'E:/1/%s.jpg' % self.num)
                        self.num = self.num + 1
                        print '已保存第%s张图片' % self.num
                        self.allImgList.append(imgurl)
                    except Exception, e:
                        print "下载图片超时"
                urllib.urlcleanup()

        except Exception, e:
            print "正则表达式异常"
        return self.num, self.allImgList