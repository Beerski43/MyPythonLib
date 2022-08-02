#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import json

def file_tree(path='.'):
    dirs = os.listdir(path)
    buf_child = []
    out_json = {
        'path': path,
        'name': '',
        'child': buf_child,
    }
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path):
            # dirの場合
            child = file_tree(dir_path)
            child['name'] = dir
            buf_child.append(child)
        else:
            # dir以外
            buf_child.append({
                'path': dir_path,
                'name': dir,
                'child': [],
            })
    return out_json

def UpdateDirJson (path_dir, path_json):
    print(path_dir)
    print(path_json)

    # JSONファイル読み込み
    with open(path_json, mode='r') as infile :
        json_old    = json.load(infile)

    # ディレクトリ構成=>JSON出力
    json_new    = file_tree(path_dir)

    if (json_old != json_new) :     # JSON比較
        # JSON更新
        with open(path_json, mode='w') as outfile :
            json.dump(json_new, outfile, indent=4)
#        print(json.dumps(json_new, indent=4))   # JSON表示
        print("JSON Update!")

        return "JSON Update!"
    else :
        # 更新なし
        print("No change")

        return "No change"

if __name__ == "__main__":

    # 引数代入
    args            = sys.argv
    out_file        = args[1]
    # ファイルパス定義
    path_dir    = os.getcwd()+"/img"
    path_json   = os.getcwd()+"/"+out_file

    UpdateDirJson(path_dir, path_json)

