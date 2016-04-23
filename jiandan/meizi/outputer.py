#coding=utf-8
'''
Created on 2016年3月13日

@author: carm
'''
import time
import uuid
import os
import urllib


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = [] #将爬取得所有数据放入内存
        
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('jiandan_meizi.html','w')
        fout.write(r"<html>")
        fout.write(r"<body>")
        fout.write(r"<table border='1'>")
        
        for page in self.datas:
            for data in page:
                fout.write(r"<tr>")
                fout.write(r"<td><img src=%s ></td>" % data)
                fout.write(r"</tr>")
        fout.write(r"</table>")
        fout.write(r"</body>")
        fout.write(r"</html>")
        
        fout.close()
        
    def save_as(self,root_dir):
        foldername = self.mkdir()
        for index,page in enumerate(self.datas):
            imgPath = root_dir+'\\%s\\%s'  % (foldername,str(index))
            for filename,imgurl in enumerate(page):
#                 UUID(Universally Unique IDentifier)是128位的全局唯一标识符，通常由32字节的字符串表示。
#                 uuid1()——基于时间戳
#                 uuid5()——基于名字的SHA-1散列值
#                 filename = str(uuid.uuid5())
                if not os.path.exists(imgPath):
                    os.makedirs(imgPath)              
                target = imgPath+"\\%s.jpg" % filename
                print "Download image to:"+target
                urllib.urlretrieve(imgurl, target)#将图片下载到指定路径中
                
                
    def mkdir(self):
        #定义文件夹的名字:年-月-日
        x = time.localtime(time.time())
        foldername = str(x.__getattribute__("tm_year"))+"-"+str(x.__getattribute__("tm_mon"))+"-"+str(x.__getattribute__("tm_mday"))
        return foldername
    
    



