#!/usr/bin/env python
#coding=utf-8
import os
import sys


all_list=[]
depend_list = []

def install(objmodule):
	cmd = "sudo easy_install -i http://g.pypi.python.org/simple %s" % objmodule
	print "SYSCMD: " , cmd
	os.system(cmd)

def load_depend():
	try:
		f = open("depend.data")
		for n in f.readlines():
			all_list.append(n.strip())
		f.close()
	except:
		print "depend.data don't exist?"
		sys.exit(-1)

def get_depend(objmodule):
	for l in all_list:
		if l.split(":")[0] == objmodule:
			d_all = l.split(":")[1].split(",")
			for d in d_all:
				if d in depend_list:
					continue
				else:
					depend_list.append(d)
			break
def find_next_depend(i):
	get_depend(depend_list[i])
	if (i+1) == len(depend_list):
		return
	find_next_depend(i+1)	

def find_all_depend(objmodule):
	get_depend(objmodule)
	if len(depend_list) == 0:
		return
	find_next_depend(0)



if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "%s modulename" % sys.argv[0]
		sys.exit(-1)
	if sys.argv[1]:

		objmodule = sys.argv[1]
		load_depend()
		find_all_depend(objmodule)
		print "%s depend module list:" % objmodule
		print depend_list
		for n in depend_list:
			install(n)
		
		install(objmodule)
