# -*- coding: UTF-8 -*-

"""一言接口，通过QQ机器人每天定时发送一句话"""

import random

import requests


# 酷推Skey(官网 cp.xuthus.cc 获得的32位Skey) 不填写则不推送失效信息
import os
skeys = os.environ['SKEY'].split('#')


def push(content):
    for key in skeys:
        if key != "":
            url = "https://push.xuthus.cc/send/" + key
            resp = requests.post(url=url, data=content).text
            print("推送结果", resp)


def run():
    url = "https://v1.hitokoto.cn/?c={}".format(
        chr(97 + random.randint(0, 11)))
    data = requests.get(url).json()
    print(data)
    # data = json.loads(resp)
    try:
        print(data['hitokoto'])
        print(data['from'])
        msg = "{}\n--from {}".format(data['hitokoto'], data['from'])
        push(msg.encode("utf-8"))
    except:
        return run()


if __name__ == '__main__':
    run()
