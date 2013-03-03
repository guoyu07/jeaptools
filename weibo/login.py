#!/usr/bin/env python
#coding=utf-8

import re
import urllib
import base64
import json
import requests
import hashlib

sha1 = lambda x : hashlib.sha1(x).hexdigest()

username = 'clkg2011@163.com'
passwd = 'sinaweibo'
WBCLIENT = 'ssplogin.js(v.1.3.18)'


session = requests.Session()
	#headers={\
	#'User-Agent':'Mozilla/5.0(ubuntn) AppleWebKit/537.1(KHT''ML,like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
#	)

resp = session.get(\
'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sina'\
'SSOController.preloginCallBack&su=%s&client=%s' % \
(base64.b64encode(username),WBCLIENT)\
	)

servertime = re.findall('"servertime":(\d*)',resp.content)
#print servertime
nonce = re.findall('"nonce":"(.*)",',resp.content)
#print nonce
pcid  = re.findall('"pcid":"(.[^A-Z]*)",',resp.content)
#print pcid

#print resp
#print resp.content
#json_str = re.findall('({.*})',resp.content)
#print json_str
#json_dict = json.loads(json_str[0])
#print json_dict
#pre_login_json = json.loads(servertime)
#print pre_login_json
username = '591508750@qq.com'
password = 'jn691121'

data = {'entry':'weibo',
	'gateway':1,
	'from':'',
	'savestate':7,
	'useticket':1,
	'ssosimplelogin':1,
	'su':base64.b64encode(urllib.quote(username)),
	'service':'mininlog',
	'servertime':servertime[0],
	'nonce':nonce[0],
	'pcid':pcid[0],
	'vsnf':'',
	'pwencode':'wsse',
	'sp':sha1(sha1(sha1(password))+str(servertime[0])+str(nonce[0])),
	'encoding':'UTF-8',
	'url':
	'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.si'
	'naSSOController.feedBackUrlCallBack',
	'returntype':'META'}

resp = session.post('http://login.sina.com.cn/sso/login.php?client=%s' % WBCLIENT,data=data)

#print resp.content

login_url = re.findall("replace\('(.*)'\)",resp.content)
#print login_url
resp = session.get(login_url[0])

#print resp.content
resp = session.get('http://s.weibo.com/weibo/python?topnav=1&wvr=5&b=1')
print resp.content


