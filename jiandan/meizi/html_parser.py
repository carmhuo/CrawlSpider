#coding=utf-8
'''
Created on 2016年3月13日

@author: carm
'''
from bs4 import BeautifulSoup
import re
import urlparse
from qiushibaike_spider.html_downloader import HtmlDownloader


class HtmlParser(object):
    
    #获取新的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #<a href="http://jandan.net/ooxx/page-1958#comments">1958</a>
        links = soup.find_all('a',href=re.compile(r'/page-\d+#comments'))
        for link in links:
            new_url = link['href'].split('?')[0]
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    #获取所需内容，返回字典形式
    def _get_new_data(self, page_url, soup):
        
        res_data = []
        imgs = soup.find_all('a',class_='view_img_link')
#         print imgs
        for img in imgs:
            #图片内容
#             print img.get('href')
            res_data.append(img.get('href'))
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding=r'utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

if __name__=='__main__':
    url = 'http://jandan.net/ooxx'
    html_doc = HtmlDownloader().download(url)
    urls,data = HtmlParser().parse(url, html_doc)
    for url in urls:
        print url 