#coding=utf-8
'''
Created on 2016年3月11日

@author: carm
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    #获取新的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/view/23131.htm
        links = soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    #获取所需内容，返回字典形式
    def _get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data['url']=page_url
        
        #title <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        #summary <div label-module="lemmaSummary" class="lemma-summary">
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding=r'utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data



