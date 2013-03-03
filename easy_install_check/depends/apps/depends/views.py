#coding=utf-8
from uliweb import expose, functions
from models import *

@expose('/')
def index():
	module_list = modules_depend.all()
	return {"module_list":module_list}

@expose('/add_depend/<id>')
def add_depend(id):
	n = modules_depend.get(modules_depend.c.id == id)
	if request.method == 'POST':
		n.depends = request.POST['depends']
		n.save()
	return redirect('/')
