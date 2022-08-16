#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import json

from lib import *

# 引数代入
#args            = sys.argv
#out_file        = args[1]
#out_file        = "img.json"
out_file        = "dirTreeImg.json"

try:
    # ファイルパス定義
#    path_dir    = "./img"
    path_dir    = "./phot"
    path_json   = "./"+out_file
    path_html   = "./index.html"

    UpdateDirJson.UpdateDirJson(path_dir, path_json)

    with open(path_html, mode='r') as infile :
        print("Content-type: text/html")
        print(infile.read())

except:
    # HTML Error画面を出す
    print("Content-type: text/html")
    print("Error.")
