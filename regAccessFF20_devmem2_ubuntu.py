#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys

cmd_rw          = "devmem2"
base_address    = "ff200000"

def regRead(addrs):
    # アドレス変換
    addrs_rd    = int(base_address, 16) + int(addrs, 16)

    # システムコールの標準出力をargs_rdに代入
    args_rd = subprocess.check_output([cmd_rw, (hex(addrs_rd)), 'w'], universal_newlines=True)
    #print (args_rd)

    # スペース削除
    args_rd = args_rd.replace(' ', '')
    # ':'で文字列を配列に区切る
    args_rd = args_rd.split(':')
    data_rd = args_rd[1].replace('0x', '')

    # 16進数 数値変換
#    num_shift   = (addrs_rd & 0x3) * 8
    data_rd     = int(data_rd, 16)
#    data_rd     = data_rd >> num_shift
    data_rd     = data_rd & 0xFF
    #print ('Read Data=', hex(data_rd))

    return data_rd

def regRead_word(addrs):
    # アドレス変換
    addrs_rd    = int(base_address, 16) + int(addrs, 16)
    #print ('address=', hex(addrs_rd))
    
    # システムコールの標準出力をargs_rdに代入
    args_rd = subprocess.check_output([cmd_rw, (hex(addrs_rd)), 'w'], universal_newlines=True)
    #print (args_rd)

    # スペース削除
    args_rd = args_rd.replace(' ', '')
    # ':'で文字列を配列に区切る
    args_rd = args_rd.split(':')
    data_rd = args_rd[1].replace('0x', '')

    # 16進数 数値変換
    data_rd     = int(data_rd, 16)
    print ('Read Data=', hex(data_rd))

    return data_rd

def regWrite_Byte(addrs, data_wr, level='null'):
    # アドレス変換
    addrs_rd    = int(addrs, 16)
    addrs_wr    = int(base_address, 16) + addrs_rd

#    res_wr      = subprocess.call([cmd_rw, (hex(addrs_wr)), 'b', hex(int(data_wr, 16))])

    # Read Modify Write
    # Register Read
    data_rd     = regRead(hex(addrs_rd))
    #print ('Read Data=', hex(data_rd))

    # データ変換
#    num_shift   = (addrs_wr & 0x3) * 8
#    data_wr     = int(data_wr, 16) << num_shift
    data_wr     = int(data_wr, 16) & 0xFF
#    mask_rd     = ~(0xFF << num_shift) & 0xFFFFFFFF
    #print ('Mask Data=', hex(mask_rd))
    if level=="H":
        data_wr     = data_rd | data_wr
    elif level=="L":
        data_wr     = data_rd & (~data_wr) & 0xFF
    else :
#        data_wr     = (data_rd & mask_rd) | data_wr
        data_wr     = data_wr

    #print ('Write Data=', hex(data_wr))
    # Register Write
    res_wr      = subprocess.call([cmd_rw, (hex(addrs_wr)), 'b', hex(data_wr)])

    return res_wr

if __name__ == "__main__":
    #print "Base Address: %s" % (base_address)
    print ('Base Address: ', base_address)
    #data_rd = regRead('0x2c1')
    #print (hex(data_rd))
    res_wd  = regWrite_Byte("2c1", "AB")
    print (res_wd)

    #data_rd = regRead_word('2c2')
    #print (hex(data_rd))

