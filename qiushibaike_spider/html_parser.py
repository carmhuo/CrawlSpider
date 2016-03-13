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
        #/view/23131.htm
        links = soup.find_all('a',href=re.compile(r'/hot/page/\d+\?s=\d+'))
        for link in links:
            new_url = link['href'].split('?')[0]
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    #获取所需内容，返回字典形式
    def _get_new_data(self, page_url, soup):
        
        res_data = []
        article_blocks = soup.find_all('div',id=re.compile(r'qiushi_tag_\d+'))
        for article_block in article_blocks:
            ab = {}
            #作者
            author = article_block.find('h2')
            #文本内容
            content = article_block.find('div',class_='content')
            #图片内容
            image_block =article_block.find('div',class_="thumb")
            if image_block is not None:
                image = image_block.find('img')
                if image is not None:
                    ab['image'] = image
            else :
                ab['image'] = None
            #点赞
            vote = article_block.find('i')
            ab['url'] = page_url
            ab['author'] = author
            ab['content'] = content
            ab['vote'] = vote
            #print author.get_text() ,content.get_text(),vote.get_text()
            res_data.append(ab)
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding=r'utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

if __name__=='__main__':
    url = 'http://www.qiushibaike.com/hot/page/1'
    html_doc = HtmlDownloader().download(url)
    urls,data = HtmlParser().parse(url, html_doc)
    for url in urls:
        print url 