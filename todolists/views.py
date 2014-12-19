from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import Context
from django.views.generic.base import TemplateView
from todolists.models import Todo
from todolists.forms import TodoForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from datetime import date

# Create your views here.
def todolist(request, stat=0, dfrom='', dto=''):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	
	allObjs = Todo.objects.filter(owner=request.user.username);
	
	stat = int(stat)
	if stat > 0 and stat < 4:
		allObjs = allObjs.filter(status=stat)
		
	return render_to_response('todolist.html',
							{'todolist':allObjs,'full_name': request.user.first_name +" " +request.user.last_name,
							'today':date.today()})
							
def create(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if request.POST:
		form = TodoForm(request.POST)
		form.owner = request.user.username
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/todolists/all')
	else:
		form = TodoForm()
		form.owner = request.user.username
	
	return render_to_response('create_todo.html',  {
		'form': form,
		'full_name': request.user.first_name +" " +request.user.last_name,
		}, context_instance=RequestContext(request))

def todo(request, todo_id = None):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	todo = Todo.objects.get(id=todo_id)
	if request.POST:
		form = TodoForm(request.POST, instance=todo)
		form.owner = request.user.username
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/todolists/all')
	else:
		form = TodoForm(instance=todo)
		form.owner = request.user.username
	
	return render_to_response('todo.html',  {
		'form': form,
		'full_name': request.user.first_name +" " +request.user.last_name
		}, context_instance=RequestContext(request))
	
def cancel_todo(request, todo_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if todo_id:
		a = Todo.objects.get(id=todo_id)
		a.status = 3
		a.save()
		
	return HttpResponseRedirect('/todolists/all')

def finish_todo(request, todo_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if todo_id:
		a = Todo.objects.get(id=todo_id)
		a.status = 2
		a.save()
		
	return HttpResponseRedirect('/todolists/all')