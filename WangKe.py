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
import re
import bs4
import requests
import urllib3
from bs4 import BeautifulSoup

print("自动获取当日网课链接程序  Ver:1.4")
print("BuildWith:Python  Author:2844829687@qq.com")

urllib3.disable_warnings()

try:
    print("正在检查更新...")
    update_url = "https://yellow-stone.tpddns.cn:8000/.%E7%BD%91%E8%AF%BE%E9%93%BE%E6%8E%A5%E8%8E%B7%E5%8F%96%E5%99%A8/latest.html"
    response = requests.get(url=update_url, verify=False)
    ver_latest = response.content.decode('utf-8')
    ver_code = requests.get(update_url, verify=False).status_code
    ver = "Ver1.4"
    #print (ver_code)
    if (ver_code == 404):
        print("无法连接服务器,请检查网络或联系开发者")
    elif (ver >= ver_latest):
        print("当前已是最新版:", ver_latest)
    elif (ver < ver_latest):
        print("当前有可用更新:", ver_latest)
    else:
        print("检查更新异常,请向开发者反馈")
except:
    print("检查更新失败")


page_url = "https://mp.weixin.qq.com/s/XaGTbzYT1VuUMB6y3V-_nQ"
cli_url = "https://cli.im/Api/Browser/deqr"


def qrcode(qrcode):

    cli_data = {"data": qrcode}

    # print(cli_data)

    response = requests.post(url=cli_url, data=cli_data)  # , verify=False

    # print(response.content.decode('utf-8'))

    qrcode_sesult = response.content.decode('utf-8')

    match_rule = re.compile(r'"RawData":"(.*?)"', re.S)

    end_page_url_disclear_list = re.findall(match_rule, qrcode_sesult)

    # print(end_page_url_disclear_list)

    end_page_url_disclear = end_page_url_disclear_list[0]

    end_page_url = end_page_url_disclear.replace('\\/', '/')

    # print(end_page_url)

    return(end_page_url)


response = requests.get(page_url)  # get原网页

classes_html = response.content.decode('utf-8')
# print(response.content.decode('utf-8'))

clsasses_html_clear = BeautifulSoup(classes_html, 'lxml')  # bs4格式化

# print(clsasses_html_clear)

classes_qrcodes = clsasses_html_clear.find('div', id="js_content")

# print(classes_qrcodes)

all_img_tag = classes_qrcodes('img')

print("今日课程列表:")

for i in range(7):
    qrcode_url = all_img_tag[i+1]['data-src']
    exec('qrcode_' + str(i+1) + ' = ' + '"'+str(qrcode_url)+'"')

    # print(all_img_tag[i+1]['data-src'])

    qrcode(eval('qrcode_' + str(i+1)))
    exec('real_url_' + str(i+1) + ' = ' + '"' +
         str(qrcode(eval('qrcode_' + str(i+1))))+'"')
    #print(eval('real_url_' + str(i+1)))

    response = requests.get(url=eval('real_url_' + str(i+1)))

    vedio_html = response.content.decode('utf-8')

    title_rule = re.compile(r'<title>(.*?)</title>', re.S)

    title_list = re.findall(title_rule, vedio_html)

    title = title_list[0]

    print(title, ':', (eval('real_url_' + str(i+1))))

input("按回车退出")
