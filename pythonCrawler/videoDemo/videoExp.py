#-*- coding:utf-8 -*-
#########################################################################
# File Name: videoExp.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python3
import requests # Network requets
import re # Regular expression
import os


def get_response(url):
    response = requests.get(url).content
    return response

def get_content(html):
    reg = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S) #matching \n
    return re.findall(reg, html)

def get_mp4_url(response):
    reg = r'data-mp4="(.*?)"'
    return re.findall(reg, response)

def get_mp4_name(response):
    reg = re.compile('<a href="/detail-.{8}.html">(.*?)</a>')
    return re.findall(re.response)

def download_mp4(mp4_url, path):
    path = ''.join(path.split())
    path = 'D:\\xx\\{}.mp4'.format(path.decode('utf-8').encode('gbk'))
    if not os.path.exisit(path):
        content = get_response(mp4_url)
        with open(path, 'wb') as f:
            f.write()
    else:
        print('Already downloaded')

def get_url_name(start_url):
    content = get_content(get_response(start_url))
    for i in content:
        if get_mp4_url(i):
            mp4_name = get_mp4_name(i)
            download_mp4(mp4_url[0], map4_name[0])
    

def main():
    for start_url in start_urls:
        get_url_name(start_url)


if __name__ == '__main__':
    start_urls = ['http://www.budejie.com/'.format(i) for i in range(10)]
    main()

