#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:58:10 2019

@author: Naifu
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

basedir = 'faces'
outdir = 'edges'
files = os.listdir(basedir)

for file in files:
    if file[0]=='.':
        continue
    else:
        filename = os.path.join(basedir,file)
        img = cv2.imread(filename,0)
        edges = cv2.Canny(img,50,300)
        
        edges = cv2.subtract(255, edges) 
        imgplot = plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image')
        plt.xticks([])
        plt.yticks([])
        
#        plt.show()
        outfilename = os.path.join(outdir,file)
        plt.savefig(outfilename)