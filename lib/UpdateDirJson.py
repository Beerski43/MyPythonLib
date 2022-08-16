#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import json

def file_tree(path='.'):
    dirs = sorted(os.listdir(path), reverse=True)   # リスト取得 & ソート
    buf_child = []
    out_json = {
        'path': path,
        'name': '',
        'attribute': '0',
        'child': buf_child,
    }
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path):
            if (
                dir != "temp" and
                dir != "Temp" and
                dir != "TEMP" and
                dir != "tmp" and
                dir != "Tmp" and
                dir != "TMP"
            ) :
#                print("\"" + dir + "\"")
                # case dir
                child = file_tree(dir_path)
                child['name'] = dir
                child['attribute'] = 0
                buf_child.append(child)
            else :
                print("除外\"" + dir + "\"")
        else:
            # case File
            # 拡張子選別
            nameFile, extFile   = os.path.splitext(dir_path)
#            print(extFile)
            if (
                extFile == ".jpeg" or
                extFile == ".jpg" or
                extFile == ".png" or
                extFile == ".gif" or
                extFile == ".bmap" or
                extFile == ".JPEG" or
                extFile == ".JPG" or
                extFile == ".PNG" or
                extFile == ".GIF" or
                extFile == ".BMAP"
            ) :
                buf_child.append({
                    'path': dir_path,
                    'name': dir,
                    'attribute': 1,
                    'child': [],
                })
            else :
                print("除外\"" + dir_path + "\"")
    return out_json

def UpdateDirJson (path_dir, path_json):
    print(path_dir)
    print(path_json)

    # ディレクトリ構成=>JSON出力
    if (os.path.isdir(path_dir)) :
        json_new    = file_tree(path_dir)
    else :
        print('directory not found('+path_dir+')')
        return -1

    # JSONファイル読み込み
    if (os.path.isfile(path_json)) :
        print("ある" + path_json)
        with open(path_json, mode='r') as infile :
            json_old    = json.load(infile)

        if (json_old != json_new) :     # JSON比較
            flag_update = True
        else :
            flag_update = False
    else :
        flag_update = True

#    print(flag_update)
    if (flag_update) :
        # JSON更新
        with open(path_json, mode='w') as outfile :
            json.dump(json_new, outfile, indent=4)
#            print(json.dumps(json_new, indent=4))   # JSON表示
        print("JSON Update!")

        return 0
    else :
        # 更新なし
        print("No change")

        return 1

if __name__ == "__main__":

    # 引数代入
    args            = sys.argv
    out_file        = args[1]
    # ファイルパス定義
    path_dir    = os.getcwd()+"/img"
    path_json   = os.getcwd()+"/"+out_file

    UpdateDirJson(path_dir, path_json)
    
