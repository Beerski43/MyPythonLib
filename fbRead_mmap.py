#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import os
import mmap
#from tqdm import tqdm

base_address    = 0xd0000000
data_length     = 0x4000000
bit_shift_frame = 26

def fbRead_mmap(reslt_h, reslt_v, bit, frame):
    # 画像格納先配列宣言
    if (bit=="8>10" or bit=="10>10"):
        img_array   = np.empty((reslt_v, reslt_h, 3), np.uint16)
    else :
        img_array   = np.empty((reslt_v, reslt_h, 3), np.uint8)

    # Offset addrese計算
    offset_address  = base_address + (frame << bit_shift_frame)

    # mmap
    fd      = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
    dram    = mmap.mmap(fd, data_length, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset = offset_address)
    dram.seek(0x0, os.SEEK_SET)

    for ii in range(reslt_v):
#    for ii in tpdm(range(reslt_v)):
        for jj in range(reslt_h):
            if bit=="10>10":
                data_rd             = dram.read(4)
                data_B              = ((data_rd[1] & 0x03) << 8) | (data_rd[0] & 0xFF)
                #print ("B=%x" % data_B)
                data_G              = ((data_rd[2] & 0x0F) << 6) | ((data_rd[1] & 0xFC) >> 2)
                #print ("G=%x" % data_G)
                data_R              = ((data_rd[3] & 0x3F) << 4) | ((data_rd[2] & 0xF0) >> 4)
                #print ("R=%x" % data_R)
            elif bit=="10>8":
                data_rd             = dram.read(4)
                data_B              = ((data_rd[1] & 0x03) << 6) | ((data_rd[0] & 0xFC) >> 2)
                #print ("B=%x" % data_B)
                data_G              = ((data_rd[2] & 0x0F) << 4) | ((data_rd[1] & 0xF0) >> 4)
                #print ("G=%x" % data_G)
                data_R              = ((data_rd[3] & 0x3F) << 2) | ((data_rd[2] & 0xC0) >> 6)
                #print ("R=%x" % data_R)
            elif bit=="8>10":
                data_rd             = dram.read(4)
                data_B              = data_rd[0] << 2
                #print ("B=%x" % data_B)
                data_G              = data_rd[1] << 2
                #print ("G=%x" % data_G)
                data_R              = data_rd[2] << 2
                #print ("R=%x" % data_R)
            else :
                data_rd             = dram.read(4)
                data_B              = data_rd[0]
                #print ("B=%x" % data_B)
                data_G              = data_rd[1]
                #print ("G=%x" % data_G)
                data_R              = data_rd[2]
                #print ("R=%x" % data_R)
            img_array[ii, jj]   = [data_B, data_G, data_R]

        #print ("v=", ii)

    return img_array

if __name__ == "__main__":
    args            = sys.argv
    reslt_h         = int(args[1], 10)
    reslt_v         = int(args[2], 10)
    bit             = args[3]
    frame           = int(args[4], 10)

    data_rd = fbRead_mmap16(reslt_h, reslt_v, bit, frame)
    print (data_rd)
