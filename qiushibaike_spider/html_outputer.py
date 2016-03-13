#coding=utf-8
'''
Created on 2016年3月13日

@author: carm
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = [] #将爬取得所有数据放入内存
        
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('qiushibaike.html','w')
        fout.write(r"<html>")
        fout.write(r"<body>")
        fout.write(r"<table border='1'>")
        
        for page in self.datas:
            for data in page:
                fout.write(r"<tr>")
                fout.write(r"<td>%s</td>" % data['url'] )
                fout.write(r"<td>%s</td>" % data['author'].encode('utf-8') )
                if data['image'] is not None:
                    fout.write(r"<td>%s %s</td>" % (data['content'].encode('utf-8'), data['image']) )
                else :
                    fout.write(r"<td>%s</td>" % data['content'].encode('utf-8') )
                fout.write(r"<td>%s</td>" % data['vote'].encode('utf-8') )
                fout.write(r"</tr>")
        fout.write(r"</table>")
        fout.write(r"</body>")
        fout.write(r"</html>")
        
        fout.close()
    
    
    
    



