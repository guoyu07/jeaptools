#coding=utf-8
import os



f = open("1.txt","r")
cmds = f.read()
f.close()

def run_browser(cmds):
	if cmds.find("上网") > -1:
		os.system("firefox www.jeapedu.com")
	if cmds.find("新浪") > -1:
		os.system("firefox www.sina.com.cn")
	if cmds.find("搜狐") > -1:
		os.system("firefox www.sohu.com")

def run_term(cmds):
	if cmds.find("终端") > -1:
		os.system("gnome-terminal")

def run_gedit(cmds):
	if cmds.find("编程") > -1:
		os.system("gedit test.py")

def run_jeap(cmds):
	count = 0
	if cmds.find("智") > -1:
		count += 1
	if cmds.find("志") > -1:
		count += 1
	if cmds.find("只") > -1:
		count += 1
	if cmds.find("支") > -1:
		count += 1
	if cmds.find("普") > -1:
		count += 1
	if cmds.find("扑") > -1:
		count += 1
	if cmds.find("谱") > -1:
		count += 1
	if count > 1:
		os.system("firefox www.jeapedu.com")

run_browser(cmds)
run_jeap(cmds)
run_term(cmds)
run_gedit(cmds)

