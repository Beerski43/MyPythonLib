#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import mmap
#from tqdm import tqdm

base_address    = 0xff300000
data_length     = 0x20000

def fbRead_mmap(reslt_h, reslt_v, bit):
    # 画像格納先配列宣言
    img_array   = np.empty((reslt_v, reslt_h, 3), np.uint8)

    # mmap
    fd      = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
    dram    = mmap.mmap(fd, data_length, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset = base_address)
    dram.seek(0x0, os.SEEK_SET)

    for ii in range(reslt_v):
#    for ii in tpdm(range(reslt_v)):
        for jj in range(reslt_h):
            if bit=="10":
                data_rd             = dram.read(4)
                data_R              = ((data_rd[1] & 0x03) << 6) | ((data_rd[0] & 0xFC) >> 2)
                #print ("R=%x" % data_R)
                data_G              = ((data_rd[2] & 0x0F) << 4) | ((data_rd[1] & 0xF0) >> 4)
                #print ("G=%x" % data_G)
                data_B              = ((data_rd[3] & 0x3F) << 2) | ((data_rd[2] & 0xC0) >> 6)
                #print ("B=%x" % data_B)
            else :
                data_rd             = dram.read(4)
                data_R              = data_rd[0]
                #print ("R=%x" % data_R)
                data_G              = data_rd[1]
                #print ("G=%x" % data_G)
                data_B              = data_rd[2]
                #print ("B=%x" % data_B)
            img_array[ii, jj]   = [data_R, data_G, data_B]

        #print ("v=", ii)

    return img_array

def ramWrite_mmap(fileMemtxt):
    with open(fileMemtxt, mode='r') as rdFile :


if __name__ == "__main__":
    data_rd = fbRead_mmap(10, 10)
    print (data_rd)
