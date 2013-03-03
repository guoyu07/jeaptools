#coding=utf-8

from uliweb.orm import *

class modules_depend(Model):
	name     = Field(str)
	depends	 = Field(str)
	mangage  = Field(str)
	status   = Field(str)
	
	
