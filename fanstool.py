#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 20:51:13
# @Author  : Mage
# @Link    : http://fengmm521.taobao.com
# @Version : $Id$

import os,sys
from magetool import urltool
import json
import time


bilibiliID = 166287840

fansUrl = 'https://api.bilibili.com/x/relation/stat?vmid=%d&jsonp=jsonp'%(bilibiliID)
viewsUrl = 'https://api.bilibili.com/x/space/upstat?mid=%d&jsonp=jsonp'%(bilibiliID)

def sayMsg(fans,views = None):
    if views:
        cmd = '/usr/bin/say 粉丝数:%d,播放数:%d'%(fans,views)
        os.system(cmd)
    else:
        cmd = '/usr/bin/say 粉丝数:%d'%(fans)
        os.system(cmd)

def main():
    # headers = {"UserAgen":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    tstr = urltool.getUrlWithChrome(fansUrl)
    tstr = urltool.conventStrTOUtf8(tstr)
    print(tstr)
    jdic = json.loads(tstr)
    # {"code":0,"message":"0","ttl":1,"data":{"mid":166287840,"following":112,"whisper":0,"black":0,"follower":95}}
    fans = jdic['data']['follower']
    time.sleep(1)
    print(viewsUrl)
    # tstr = urltool.getUrlWithChrome(viewsUrl)
    # tstr = urltool.conventStrTOUtf8(tstr)
    # print(tstr)
    # # {"code":0,"message":"0","ttl":1,"data":{"archive":{"view":8386},"article":{"view":0}}}
    # jdic = json.loads(tstr)

    # views = jdic['data']['archive']['view']
    # sayMsg(fans,views)
    sayMsg(fans)

if __name__ == '__main__':
    main()
    
