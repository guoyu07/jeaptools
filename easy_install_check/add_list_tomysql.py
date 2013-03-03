#coding=utf-8

from uliweb.orm import *

db = get_connection('mysql://root:root@localhost/depends?charset=utf8')

class modules_depend(Model):
	name     = Field(str)
	depends	 = Field(str)
	mangage  = Field(str)
	status   = Field(str)


if __name__ == "__main__":
	
	db.metadata.create_all()
	f = open("modules.list")
	buf = f.readlines()
	f.close()
	for n in buf:
		b = modules_depend()
		b.name = n.strip()
		b.save()

