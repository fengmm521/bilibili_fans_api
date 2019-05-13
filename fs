#!/bin/bash
export PATH=/usr/local/bin/:/bin:/usr/bin:$PATH
CUR_PATH=`pwd`
basepath=$(cd `dirname $0`; pwd)
echo $CUR_PATH
echo $basepath

python ~/Documents/github/bilibili_fans_api/fanstool.py