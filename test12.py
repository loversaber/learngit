#!/usr/bin/env python
#python3.4 test12.py /home/bioinfo/liuqi/ped/info/change_end
from collections import defaultdict
from sys import argv
import os
import shutil
with open(argv[1],'rt') as f:
 d={}
 for line in f:
  population=line.split()[0]
  number=line.split()[1]
  if population not in d.keys():
   d[population]=[]
  d[population].append(number)   

path_now=os.getcwd()   
path='/home/bioinfo/liuqi/heter_smarker_share/share_s_h'
fil=os.listdir(path)
#print (fil[1])
for k,v in d.items():
 try:
  di=os.mkdir(k+"_1")
 except FileExistsError:
  pass
dii=os.listdir(path_now)
for k,v in d.items():
 for x in v:
  if x in fil:
   os.system("cp "+path+"/"+x+" ./"+k+"_1")
2017年 5月16日 星期二 22时53分49秒 CST
