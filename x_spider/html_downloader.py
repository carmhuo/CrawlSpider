#coding=utf-8
'''
Created on 2016年3月11日

@author: carm
'''
import urllib2
from qiushibaike_spider.html_parser import HtmlParser


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0'
        headers = {'User-Agent':user_agent}
        try:
            request = urllib2.Request(url,headers=headers)
            response = urllib2.urlopen(request)
        except urllib2.URLError,e:
            if response.getcode()!= 200:
                return e.code+':'+e.reason
        
        return response.read()
        
        
        
if __name__ == '__main__':
    url ='http://baike.baidu.com/view/21087.htm'
    downloader = HtmlDownloader()
    html_doc = downloader.download(url)
    parser = HtmlParser()        
    data = parser.parse(url, html_doc)
    



