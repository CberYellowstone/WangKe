#!/usr/bin/env python
# coding: utf-8

'''
                     _ooOoo_
                    o8888888o
                    88" . "88
                    (| -_- |)
                     O\ = /O
                 ____/`---'\____
               .   ' \\| |// `.
                / \\||| : |||// \
              / _||||| -:- |||||- \
                | | \\\ - /// | |
              | \_| ''\---/'' | |
               \ .-\__ `-` ___/-. /
            ___`. .' /--.--\ `. . __
         ."" '< `.___\_<|>_/___.' >'"".
        | | : `- \`.;`\ _ /`;.`/ - ` : | |
          \ \ `-. \_ __\ /__ _/ .-` / /
  ======`-.____`-.___\_____/___.-`____.-'======
                     `=---='
 
  .............................................
           佛祖保佑             永无BUG
'''
print ("自动获取当日网课链接程序  Ver:1.3")
print ("BuildWith:Python  Author:2844829687@qq.com")
print ("Loading...")

import requests
import re
import bs4
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()


page_url = "https://mp.weixin.qq.com/s/XaGTbzYT1VuUMB6y3V-_nQ"
cli_url="https://cli.im/Api/Browser/deqr"


def qrcode(qrcode):

    cli_data={"data":qrcode}

    #print(cli_data)

    response = requests.post(url=cli_url,data=cli_data) #, verify=False

    #print(response.content.decode('utf-8'))

    qrcode_sesult = response.content.decode('utf-8')

    match_rule = re.compile(r'"RawData":"(.*?)"', re.S)

    end_page_url_disclear_list = re.findall(match_rule,qrcode_sesult)

    #print(end_page_url_disclear_list)

    end_page_url_disclear=end_page_url_disclear_list[0]

    end_page_url=end_page_url_disclear.replace('\\/','/')

    #print(end_page_url)
    
    return(end_page_url)




response = requests.get(page_url)#get原网页

classes_html = response.content.decode('utf-8')
#print(response.content.decode('utf-8'))

clsasses_html_clear = BeautifulSoup(classes_html, 'lxml')#bs4格式化

#print(clsasses_html_clear)

classes_qrcodes = clsasses_html_clear.find('div', id="js_content")

#print(classes_qrcodes)

all_img_tag = classes_qrcodes('img')


for i in range(7):
    qrcode_url = all_img_tag[i+1]['data-src']
    exec('qrcode_' + str(i+1) + ' = ' + '"'+str(qrcode_url)+'"')
    
    #print(all_img_tag[i+1]['data-src'])
        
    qrcode(eval('qrcode_' + str(i+1)))
    exec('real_url_' + str(i+1) + ' = ' + '"'+str(qrcode(eval('qrcode_' + str(i+1))))+'"')
    #print(eval('real_url_' + str(i+1)))
    
    response = requests.get(url=eval('real_url_' + str(i+1)))
    
    vedio_html = response.content.decode('utf-8')
    
    title_rule = re.compile(r'<title>(.*?)</title>',re.S)
    
    title_list = re.findall(title_rule,vedio_html)
    
    title = title_list[0]
    
    print(title,':',(eval('real_url_' + str(i+1))))

input("任意键退出")