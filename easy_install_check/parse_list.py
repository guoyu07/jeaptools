#!/usr/bin/env python
#coding=utf-8
import re

all_list=[]
f = open("pypi.list")
buf = f.read()
f.close()

l = re.findall("<a.*>(.*)</a>",buf)

for n in l:
	a = re.search("(.*)&nbsp",n)
	all_list.append(a.group(1))
	
all_list = list(set(all_list))
for n in all_list:
	print n
