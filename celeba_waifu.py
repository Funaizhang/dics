#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:15:09 2019

@author: Naifu
"""

import numpy as np
import os
from shutil import copyfile


indir = 'img_align_celeba'
outdir = 'celeba_waifu'
att_txt = 'list_attr_celeba.txt'
max_img = 25000

#d = {}
with open(att_txt) as f:
    count = 0
    for line in f:
        line_arr = line.split()
        if len(line_arr)>21 and line_arr[21] == "-1": #line_arr[21] indicates male/female
            input_name = os.path.join(indir, line_arr[0])
            output_name = os.path.join(outdir, line_arr[0])
            print(output_name)
            copyfile(input_name, output_name)
            count += 1
        if count > max_img:
            break
