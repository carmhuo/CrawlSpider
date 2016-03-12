#coding=utf-8
'''
Created on 2016年3月11日

@author: carm
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
        
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html','w')
        fout.write(r"<html>")
        fout.write(r"<body>")
        fout.write(r"<table border='1'>")
        
        for data in self.datas:
            fout.write(r"<tr>")
            fout.write(r"<td>%s</td>" % data['url'] )
            fout.write(r"<td>%s</td>" % data['title'].encode('utf-8') )
            fout.write(r"<td>%s</td>" % data['summary'].encode('utf-8') )
            fout.write(r"</tr>")
        fout.write(r"</table>")
        fout.write(r"</body>")
        fout.write(r"</html>")
        
        fout.close()
    
    
    
    



