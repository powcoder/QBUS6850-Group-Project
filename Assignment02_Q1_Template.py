https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 01:19:24 2018

@author: QBUS6850 Team
An example to load this csv file


"""
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import decomposition


def load_this(input_dir):
    
    reviews = pd.read_csv(input_dir, encoding="utf-8",sep = ";")
    
    return reviews

input_dir = "./Sydney_Reviews.csv"
reviews = load_this(input_dir)


# Your code here


 
