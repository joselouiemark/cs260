from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse
from cs260.forms import MyRegistrationForm

def login(request):
	c = {}
	c.update(csrf(request))
	c.update({'title':'Login'})
	return render_to_response('login.html',c)
	
def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	
	args = {}
	
	args['form'] = MyRegistrationForm()
	
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')