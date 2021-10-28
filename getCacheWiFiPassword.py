# windows
# 简体中文，中间用到正则表达式，我不知道在别的系统语言下
# 关键字是什么。


import os
import re

# netsh wlan show profile
# netsh wlan show profile “WiFi名称” key=clear

wifi_info = os.popen('netsh wlan show profile').read()
wifi_list = re.findall(r'.+:\s(\S+)', wifi_info)


def get_wifi_password(wifi):
    data = os.popen(f'netsh wlan show profile {wifi} key=clear').read()
    password_list = re.findall(r'关键内容.+:\s(.+)', data)
    if password_list:
        password = password_list[0]
    else:
        password = ''
    return password

print('{:<20s}{:<20s}'.format('WIFI', 'PASSWORD'))
for wifi in wifi_list:
    print('{:<20s}{:<20s}'.format(wifi, get_wifi_password(wifi)).strip())

os.system('pause')
