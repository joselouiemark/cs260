from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import Context
from django.views.generic.base import TemplateView
from todolists.models import Todo
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from datetime import date

# Create your views here.
def todolist(request):
    if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	
	allObjs = Todo.objects.filter(owner=request.user.username);
	
	if stat > 0 and stat < 4:
		allObjs = allObjs.filter(status=stat)
		
	return render_to_response('todolist.html',
							{'todolist':allObjs,'full_name': request.user.first_name +" " +request.user.last_name,
							'today':date.today()})