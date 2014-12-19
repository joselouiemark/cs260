from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse

def login(request):
	c = {}
	c.update(csrf(request))
	c.update({'title':'Login'})
	return render_to_response('login.html',c)