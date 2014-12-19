from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.test.client import RequestFactory
from django.test.client import Client
from datetime import date
from datetime import datetime

#from todolists.views import home_page

from cs260.views import login
from cs260.views import auth_view
from cs260.views import loggedin
from cs260.views import invalid_login
from cs260.views import logout
from cs260.views import register_user
from cs260.views import register_success

class HomePageTest(TestCase):
	def setUp(self):
		# Every test needs access to the request factory.
		self.factory = RequestFactory()
		self.user = User.objects.create_user(
			username='joselouiemark', password='rockon1038', first_name='louie', last_name='ano',)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = login(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>To-Do</title>', response.content)
		# there is an login form in the home page
		self.assertIn(b'<input type="submit" value="login" />', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
		
	def test_register_page_returns_correct_html(self):
		request = HttpRequest()
		response = register_user(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>Register</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
	
	def test_register_can_save_a_user_registration(self):
		request = HttpRequest()
		request.method = 'POST'
		#sample user details
		request.POST['username'] = 'louie'
		request.POST['first_name'] = 'louie'
		request.POST['last_name'] = 'ano'
		request.POST['email'] = 'louie@louie.com'
		request.POST['password1'] = 'louie'
		request.POST['password2'] = 'louie'
		
		#register this user
		response = register_user(request)
		
		#determine success if it redirects to register_success
		self.assertEqual(response['location'], '/accounts/register_success')
	
	def test_register_success(self):
		#tests register success page
		request = HttpRequest()
		#get simulated user
		request.user = self.user
		response = register_success(request)
		#should have this message
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>Register Success</title>', response.content)
		self.assertIn(b'You have registered', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))

	def test_login_user(self):
		#tests login user page page
		request = HttpRequest()
		response = login(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<input type="submit" value="login" />', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
		
	def test_login_fail_user_authentication(self):
		#tests that it would go to fail page if not successfully loggedin
		request = HttpRequest()
		request.method = 'POST'
		#use admin
		request.POST['username'] = 'invaliduser'
		request.POST['password'] = 'invaliduserpwd'
		#should be redirected to all to-dos
		response = auth_view(request)
		self.assertEqual(response['location'], '/accounts/invalid')
		
	def test_loggedin_page(self):
		#tests the logged in page
		request = HttpRequest()
		#get simulated user
		request.user = self.user
		response = loggedin(request)
		#should have this message
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'you are now logged in!', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
	
	def test_invalid_login(self):
		#tests that it would go to fail page if not successfully loggedin
		request = HttpRequest()
		#get simulated user
		request.user = self.user
		response = invalid_login(request)
		#should have ask user to login again
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<input type="submit" value="login" />', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
	
		
		
		
