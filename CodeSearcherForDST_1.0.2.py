# -*- coding: utf-8 -*-
"""
CodeSearcher For Don't Starve Together Players

Created on Sun May  3 01:18:39 2020

@author: Steve.D.Jobs

Copyright (c) 2020 Steve D. J..All rights reserved.
"""

print("Copyright (c) 2020 Steve D. J..All rights reserved.\n")
print("欢迎使用CodeSearcher For Don't Starve Together!\n本程序须与Don't Starve Together.xlsx配套使用。")

import pandas as pd
from pandas import DataFrame

codebase=pd.read_excel("Don't Starve Together.xlsx",index_col = None,colNames = 0)

def getname():
    global name
    name = input("输入要查询的关键词\n")
    name = list(name)

def searcher():
    #global paper
    paper = DataFrame([['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']],columns = ['Name','Code'])
    ct = 0
    for i in range(0,codebase.shape[0]-1):
        CN_name = codebase.loc[i,'CNname']
        CN_name_list = list(CN_name)
        for j in CN_name_list:
            for k in name:
                if j == k:
                    paper.loc[ct,'Name'] = CN_name
                    paper.loc[ct,'Code'] = codebase.loc[i,'code']
                    ct = ct+1
    if paper.iloc[0,0] != '':
        print(paper)
    else:
        print("Not Found!")

def searcher_adv():
    #global paper
    paper = DataFrame([['','']],columns = ['Name','Code'])
    ct = 0
    length=len(name)
    #print(length)
    for i in range(0,codebase.shape[0]-1):
        CN_name = codebase.loc[i,'CNname']
        CN_name_list = list(CN_name)
        flag = 0
        for j in name:
            if flag < length:
               for k in CN_name_list:
                   if j == k:
                       flag = flag+1
        if flag >= length:
            paper.loc[ct,'Name'] = CN_name
            paper.loc[ct,'Code'] = codebase.loc[i,'code']
            ct =ct+1
    if paper.iloc[0,0] != '':
        print(paper)
    else:
        print("Not Found!")

mod = 'C'
while (mod != 'A') and (mod != 'B'):
    print("请选择要使用的查找方法\n")
    mod = input("A:给我所有包含关键字的代码\nB:标准查找法\n")
if mod == 'A':
    while True:
        getname()
        searcher()   
if mod == 'B':
    while True:
        getname()
        searcher_adv()   