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
import ctypes
import sys


input_len = len(sys.argv)
no_window = False
if ("--no-window" in sys.argv):
    input_len = len(sys.argv) - 1
    no_window = True
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)

import os
import re
import webbrowser
from time import sleep
import bs4
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()


print("自动获取当日网课链接程序  Ver:1.7")
print("BuildWith:Python  Author:2844829687@qq.com")
print("")

try:
    print("正在检查更新...")
    update_url = "https://yellow-stone.tpddns.cn:8000/.%E7%BD%91%E8%AF%BE%E9%93%BE%E6%8E%A5%E8%8E%B7%E5%8F%96%E5%99%A8/updates.html"
    response = requests.get(url=update_url, verify=False)
    update_html = response.content.decode('utf-8')
    ver_rule = re.compile(r'<Ver>(.*?)</Ver>', re.S)
    ver_latest = re.findall(ver_rule, update_html)[0]
    ver_gui_rule = re.compile(r'<GUI>(.*?)</GUI>', re.S)
    ver_gui_latest = re.findall(ver_gui_rule, update_html)[0]
    download_url_rule = re.compile(r'<DL>(.*?)</DL>', re.S)
    download_url = re.findall(download_url_rule, update_html)[0]
    GUI_download_url_rule = re.compile(r'<GDL>(.*?)</GDL>', re.S)
    GUI_download_url = re.findall(GUI_download_url_rule, update_html)[0]
    download_name_rule = re.compile(r'<DLN>(.*?)</DLN>', re.S)
    download_name = re.findall(download_name_rule, update_html)[0]
    shout_rule = re.compile(r'<SHOUT>(.*?)</SHOUT>', re.S)
    shout = re.findall(shout_rule, update_html)[0]

    if (shout != ""):
        print("")
        print("在线公告:",shout)
        print("")


    ver_code = requests.get(update_url, verify=False).status_code
    ver = "Ver1.7"
    # print (ver_code)
    if (ver_code != 200):
        print("无法连接服务器,请检查网络或联系开发者")
        print("")
    elif (ver >= ver_latest):
        print("当前已是最新版:", ver_latest)
        print("")
    elif (ver < ver_latest):
        print("当前有可用更新:", ver_latest)
        print("")
        print("正在下载最新版本:", ver_latest)
        download_main = requests.get(download_url, verify=False)
        with open(download_name, "wb") as code:
            code.write(download_main.content)
        print("最新版:", ver_latest, "已下载")
        print("")
        sys.exit()
    else:
        print("检查更新异常,请向开发者反馈")
        print("")
except:
    print("检查更新失败,未知错误,请联系开发者")
    print("")

try:
    os.remove("网课链接获取器_Ver1.6.exe")
    os.remove("网课链接获取器_Ver1.5.exe")
except:
    pass


def end_program(pro_name):
            os.popen("taskkill /f /im " + pro_name)
            #os.system("taskkill /f /im " + pro_name)
            print ("进程",pro_name,"已结束")


if (no_window == True):
    print("已进入到GUI更新模式")
    def getexever(exe_name):
        print("pyi-grab_version " + exe_name + " GUI_version_file")
        os.system("pyi-grab_version " + exe_name + " GUI_version_file")
        ver_gui_rule = re.compile(r"'FileVersion', u'(.*?)'", re.S)
        with open("GUI_version_file", "r",encoding=('utf-8')) as f:  # 打开文件
            GUI_version_file_read = f.read()  # 读取文件
        ver_gui = re.findall(ver_gui_rule, GUI_version_file_read)[0]
        os.remove("GUI_version_file")
        return ver_gui
    print("正在获取GUI版本")
    ver_gui = getexever("网课链接获取器_GUI.exe")
    print("已获取到GUI版本:",ver_gui)
    print("GUI最新版本:",ver_gui_latest)
    if (ver_gui < ver_gui_latest):
        print ("检测到GUI需要更新")
        try:
            print("正在尝试关闭GUI")
            end_program("网课链接获取器_GUI.exe")
            print("正在尝试删除GUI")
            sleep(2)
            os.remove("网课链接获取器_GUI.exe")
            print("GUI已删除")
            download_GUI = requests.get(GUI_download_url, verify=False)
            print("正在下载GUI")
            with open("网课链接获取器_GUI.exe", "wb") as code:
                code.write(download_GUI.content)
            print("GUI已下载完成,正在尝试唤起GUI")
            os.startfile("网课链接获取器_GUI.exe")
            print("GUI已唤起")
        except:
            pass
        finally:
            sys.exit()

browser_check = True

#print (len(sys.argv))

if ("--output" in sys.argv):
    output_file = open("OutPut.txt", 'w+', encoding="ANSI")
    print("本次将会将结果输出至OutPut.txt")
    print("")
    if ("--silent" in sys.argv):
        browser_check = False
        print("本次将不会询问是否使用默认浏览器打开链接")
        print()
        if (input_len >= 4):
            print("错误,未识别的参数", sys.argv, "请检查后重试")
            print("")
            input("按回车退出")
            sys.exit()
    elif (input_len >= 3):
        print("错误,未识别的参数", sys.argv, "请检查后重试")
        print("")
        input("按回车退出")
        sys.exit()
elif ("--silent" in sys.argv):
    if (browser_check == True):
        if (input_len >= 3):
            print("错误,未识别的参数", sys.argv, "请检查后重试")
            print("")
            input("按回车退出")
            sys.exit()
        else:
            browser_check = False
            print("本次将不会询问是否使用默认浏览器打开链接")
            print()
elif ("--no-window" in sys.argv):
    browser_check = False
    output_file = open("OutPut.txt", 'w+', encoding="ANSI")
    if (input_len >= 2):
        print("错误,未识别的参数", sys.argv, "请检查后重试")
        print("")
        input("按回车退出")
        sys.exit()
elif (input_len == 1):
    pass
    #print (input_len)
else:
    print("错误,未识别的参数", sys.argv, "请检查后重试")
    print("")
    input("按回车退出")
    sys.exit()

#print (browser_check)

page_url = "https://mp.weixin.qq.com/s/XaGTbzYT1VuUMB6y3V-_nQ"
cli_url = "https://cli.im/Api/Browser/deqr"
real_url_1 = ""
real_url_2 = ""
real_url_3 = ""
real_url_4 = ""
real_url_5 = ""
real_url_6 = ""
real_url_7 = ""


def style(str):
    str = str.replace("第一", "第1")
    str = str.replace("第二", "第2")
    str = str.replace("第三", "第3")
    str = str.replace("第四", "第4")
    str = str.replace("第五", "第5")
    str = str.replace("第六", "第6")
    str = str.replace("第七", "第7")
    str = str.replace("第八", "第8")
    str = str.replace("第九", "第9")
    str = str.replace("政治第", "政治 第")
    str = str.replace("历史第", "历史 第")
    str = str.replace("地理第", "地理 第")
    str = str.replace("生物第", "生物 第")
    str = str.replace("数学第", "数学 第")
    str = str.replace("语文第", "语文 第")
    str = str.replace("英语第", "英语 第")
    str = str.replace("化学第", "化学 第")
    str = str.replace("物理第", "物理 第")
    str = str.replace("_"," ")
    str = str.replace("节 ","节")
    str = str.replace("节","节 ")
    return str


def qrcode(qrcode):

    cli_data = {"data": qrcode}

    # print(cli_data)

    response = requests.post(url=cli_url, data=cli_data)  # , verify=False

    # print(response.content.decode('utf-8'))

    qrcode_result = response.content.decode('utf-8')

    result_match_rule = re.compile(r'"RawData":"(.*?)"', re.S)

    end_page_url_disclear_list = re.findall(result_match_rule, qrcode_result)

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
print("")

titles_list = list()
links_list = list()

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

    title_find_list = re.findall(title_rule, vedio_html)

    title = style(title_find_list[0])

    out_finally = title + ' : ' + (eval('real_url_' + str(i+1)))

    #print(title, ':', (eval('real_url_' + str(i+1))))

    print(out_finally)

    titles_list.append(out_finally+"\n")
    links_list.append(eval('real_url_' + str(i+1)) + "\n")
    #print (titles_list)

try:
    output_file.writelines(titles_list)
    if (no_window == True):
        output_file.writelines(links_list)
        output_file.write(shout)
    output_file.close()
except:
    pass

openbrowser_check_times = 0
gradecheck_times = 0


def openbrowser_check():
    global openbrowser_check_times
    openbrowser_check_times = openbrowser_check_times + 1
    print("")
    openbrowser = input("是否使用默认浏览器打开链接?(y/n):")
    if (openbrowser == 'y') or (openbrowser == 'yes') or (openbrowser == 'Y') or (openbrowser == 'YES'):
        gradecheck_times = 0

        def gradecheck():
            grade = input("请输入年级:(7/8/9):")
            global gradecheck_times
            gradecheck_times = gradecheck_times + 1
            if (grade == "7"):
                webbrowser.open(real_url_1)
                webbrowser.open(real_url_2)
            elif (grade == "8"):
                webbrowser.open(real_url_3)
                webbrowser.open(real_url_4)
            elif (grade == "9"):
                webbrowser.open(real_url_5)
                webbrowser.open(real_url_6)
                webbrowser.open(real_url_7)
            elif (gradecheck_times == 3):
                print("")
                print("错误次数太多,已取消")
                print("")
                input("按回车退出")
                sys.exit()
            else:
                print("格式错误,请重新输入")
                gradecheck()
        gradecheck()
    elif (openbrowser == 'n') or (openbrowser == 'no') or (openbrowser == 'N') or (openbrowser == 'NO'):
        pass
    elif (openbrowser_check_times == 3):
        print("")
        print("错误次数太多,已取消")
        print("")
        input("按回车退出")
        sys.exit()
    else:
        print("格式错误,请重新输入")
        openbrowser_check()


if (browser_check == True):
    openbrowser_check()
else:
    pass


if (no_window == False):
    print("")
    sleep(0.6)
    input("按回车退出")
sys.exit()
