#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def pixelConv_RGB8bit(fbData):
    # 16進数 数値変換
    data_rd = int(fbData, 16)
    #print "data=%x" % (data_rd)
    dataR   = ((data_rd >> 22) & 0xFF)
    dataG   = ((data_rd >> 12) & 0xFF)
    dataB   = ((data_rd >> 2) & 0xFF)

    return [dataR, dataG, dataB]

if __name__ == "__main__":
    args_px = pixelConv_RGB8bit("240951e0")
    print ("R=%x/G=%x/B=%x" % (args_px[0], args_px[1], args_px[2]))
