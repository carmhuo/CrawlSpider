#coding=utf-8
'''
Created on 20160313

@author: carm
'''
from qiushibaike_spider import url_manager, html_downloader, html_parser, html_outputer


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
                self.outputer.collect_data(new_data) #收集所有数据放入内存
                
                if count == 50:
                    break
                count = count +1
            except:
                print 'crawl failed'
        #输出到html文件
        self.outputer.output_html()



if __name__ == "__main__":
    #爬糗事百科热门段子
    page = 1  #当前页    
    root_url="http://www.qiushibaike.com/hot/page/"+str(page)
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
    
