#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:15:09 2019

@author: Naifu
"""

import numpy as np
import argparse
import os
from shutil import copyfile

indir = 'img_align_celeba'
outdir = 'celeba_waifu'
att_txt = 'list_attr_celeba.txt'
max_img = 25000

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', default='img_align_celeba', help='input CelebA folder path')
    parser.add_argument('-output', default='celeba_waifu', help='output folder path')
    parser.add_argument('-attr', default='list_attr_celeba.txt', help='CelebA attributes file path')
    parser.add_argument('-max', type=int, default=None, help='Maximum number of samples to copy')
    args = parser.parse_args()

    with open(args.attr) as f:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        count = 0
        for line in f:
            line_arr = line.split()
            if len(line_arr)>21 and line_arr[21] == "-1": #line_arr[21] indicates male/female
                input_name = os.path.join(args.input, line_arr[0])
                output_name = os.path.join(args.output, line_arr[0])
                print(output_name)
                copyfile(input_name, output_name)
                count += 1
            if args.max is not None and count > args.max:
                break
