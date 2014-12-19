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
from datetime import timedelta
from datetime import datetime
from datetime import date

# Create your views here.
def todolist(request, stat=0, dfrom='', dto='', range=''):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	
	if request.POST:
		sdate = request.POST.get('sdate', '')
		edate = request.POST.get('edate', '')
		type = request.POST.get('type', 1)
		
		sdateStr = '0'
		edateStr = '0'
		typeStr = '0'
		
		if sdate not in [None, '']:
			sdateStr = datetime.strptime(dfrom, '%Y-%m-%d' ).strftime('%Y%m%d')

		if edate not in [None, '']:
			edateStr = datetime.strptime(dto, '%Y-%m-%d' ).strftime('%Y%m%d')

		if type not in [None, '']:
			typeStr = str(type)
		
		return HttpResponseRedirect('/todolists/all/'+typeStr+'/'+sdateStr+'/'+edateStr+'/0')
	
	sdateobj = date.today()
	edateobj = date.today()
	
	if range not in [None, '', '0']:
		if range in ['1'] : #by month
			sdateobj = datetime.strptime(datetime.strftime(date.today(), '%Y-%m-01' ), '%Y-%m-%d')
			edateobj = datetime.strptime(datetime.strftime(date.today(), '%Y-%m-30' ), '%Y-%m-%d')
		elif range in ['2'] : #by week
			day = date.today();
			day_of_week = day.weekday()

			to_beginning_of_week = timedelta(days=day_of_week)
			beginning_of_week = day - to_beginning_of_week

			to_end_of_week = timedelta(days=6 - day_of_week)
			end_of_week = day + to_end_of_week
			
			sdateobj = beginning_of_week
			edateobj = end_of_week
	
	allObjs = Todo.objects.filter(owner=request.user.username);
	allObjs.filter(status=1).filter(date__lt=sdateobj).update(date=edateobj)
	stat = int(stat)
	if stat > 0 and stat < 4:
		allObjs = allObjs.filter(status=stat)
	
	datedisplay = ''
	if sdateobj not in [None, '', '0'] or edateobj not in [None, '', '0'] :
		datedisplay = datetime.strftime(sdateobj, '%Y-%m-%d') + " - " + datetime.strftime(edateobj, '%Y-%m-%d')
	else :
		datedisplay = date.today()
	
	return render_to_response('todolist.html',
							{'todolist':allObjs,'full_name': request.user.first_name +" " +request.user.last_name,
							'datedisplay':datedisplay, 'statuscode':stat})
							
def create(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if request.POST:
		form = TodoForm(request.POST)
		#form.owner = request.user.username
		if form.is_valid():
			form.save(request.user.username)
			
			return HttpResponseRedirect('/todolists/all')
	else:
		form = TodoForm()
		#form.owner = request.user.username
	
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
		#form.owner = request.user.username
		if form.is_valid():
			form.save(request.user.username)
			
			return HttpResponseRedirect('/todolists/all')
	else:
		form = TodoForm(instance=todo)
		#form.owner = request.user.username
	
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