#coding=utf-8
'''
Created on 20160311

@author: carm
'''
from x_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  #初始化url管理器
        self.downloader = html_downloader.HtmlDownloader() #初始化下载器
        self.parser = html_parser.HtmlParser() #初始化解析器
        self.outputer = html_outputer.HtmlOutputer()  #初始化输出
    
    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  
                print "crawl %d : %s" %(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 100:
                    break
                count = count +1
            except:
                print 'crawl failed'
        
        self.outputer.output_html()



if __name__ == "__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
    
