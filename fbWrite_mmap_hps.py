#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import mmap

base_address    = 0x3f100000
data_length     = 0x4000000
bit_shift_frame = 26

def fbWrite_mmap_hps(img_array, reslt_h, reslt_v, bit):
#    # 画像格納先配列宣言
#    img_array   = np.empty((reslt_v, reslt_h, 3), np.uint8)

    # Offset addrese計算
    offset_address  = base_address

    # mmap
    fd      = os.open("/dev/mem", os.O_RDWR | os.O_SYNC)
    dram    = mmap.mmap(fd, data_length, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset = offset_address)
    dram.seek(0x0, os.SEEK_SET)
#    data_wr = []

    for ii in range(reslt_v):
        for jj in range(reslt_h):
            data_B, data_G, data_R  = img_array[ii, jj]

#            data_0  = img_array[ii, jj, 0]
#            data_1  = img_array[ii, jj, 1]
#            data_2  = img_array[ii, jj, 2]
#            print ("%d, %d, %x-%x, %x, %x" % (jj, ii, data_R, data_0, data_G, data_B))

            if bit=="8>10":
                data_wr_0   = (data_B << 2) & 0x0FF
                data_wr_1   = (data_G << 4) & 0xF0 | (data_B >> 6) & 0x03
                data_wr_2   = (data_R << 6) & 0xC0 | (data_G >> 4) & 0x0F
                data_wr_3   = (data_R >> 2) & 0x3F

            elif bit=="10>10":
                data_wr_0   = data_B & 0x0FF
                data_wr_1   = (data_G << 2) & 0xFC | (data_B >> 8) & 0x03
                data_wr_2   = (data_R << 4) & 0xF0 | (data_G >> 6) & 0x0F
                data_wr_3   = (data_R >> 4) & 0x3F

            elif bit=="10>8":
                data_wr_0   = data_B >> 2
                data_wr_1   = data_G >> 2
                data_wr_2   = data_R >> 2
                data_wr_3   = 0x00

            else :
                data_wr_0   = data_B
                data_wr_1   = data_G
                data_wr_2   = data_R
                data_wr_3   = 0x00

            dram.write_byte(data_wr_0)
            dram.write_byte(data_wr_1)
            dram.write_byte(data_wr_2)
            dram.write_byte(data_wr_3)

#            data_wr.append([data_wr_0, data_wr_1, data_wr_2, data_wr_3])
#    dram.write(data_wr)

if __name__ == "__main__":
    fbWrite_mmap_hps()
