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

#todolists app views
#from todolists.views import home_page

#general views
from cs260.views import login
from cs260.views import auth_view
from cs260.views import loggedin
from cs260.views import invalid_login
from cs260.views import logout
from cs260.views import register_user
from cs260.views import register_success

#models
from todolists.models import Todo

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
	
	def test_saving_and_retrieving_todos(self):
		#tests listing of all todos regardless of the type
		#first create records, specifically three of them (a waiting, a cancelled and a finished)
		
		form1 = Todo()
		form1.title = 'sample title one'
		form1.summary = 'sample summary one'
		form1.date = '2014-12-29'
		form1.status = 1
		form1.save()
		
		form2 = Todo()
		form2.title = 'sample title two'
		form2.summary = 'sample summary two'
		form2.date = '2014-12-29'
		form2.status = 2
		form2.save()
		
		form3 = Todo()
		form3.title = 'sample title three'
		form3.summary = 'sample summary three'
		form3.date = '2014-12-29'
		form3.status = 3
		form3.save()
		
		savedTodos = Todo.objects.all()
		self.assertEqual(savedTodos.count(), 3)
		
		first_saved_todo= savedTodos[0]
		second_saved_todo = savedTodos[1]
		third_saved_todo = savedTodos[2]
		self.assertEqual(first_saved_todo.title, 'sample title one')
		self.assertEqual(first_saved_todo.summary, 'sample summary one')
		self.assertEqual(first_saved_todo.status, 1)
		self.assertEqual(second_saved_todo.title, 'sample title two')
		self.assertEqual(second_saved_todo.summary, 'sample summary two')
		self.assertEqual(second_saved_todo.status, 2)
		self.assertEqual(third_saved_todo.title, 'sample title three')
		self.assertEqual(third_saved_todo.summary, 'sample summary three')
		self.assertEqual(third_saved_todo.status, 3)
		
	def test_saving_and_retrieving_todos_with_filter(self):
		#tests listing of all todos with filtering
		#first create records, specifically three of them (a waiting, a cancelled and a finished)
		
		form1 = Todo()
		form1.title = 'sample title waiting'
		form1.summary = 'sample summary waiting'
		form1.date = '2014-12-29'
		form1.status = 1
		form1.save()
		
		form2 = Todo()
		form2.title = 'sample title finished'
		form2.summary = 'sample summary finished'
		form2.date = '2014-12-29'
		form2.status = 2
		form2.save()
		
		form3 = Todo()
		form3.title = 'sample title cancelled'
		form3.summary = 'sample summary cancelled'
		form3.date = '2014-12-29'
		form3.status = 3
		form3.save()
		
		savedTodos = Todo.objects.all()
		
		allObjsFilterWaiting = savedTodos.filter(status=1)
		self.assertEqual(allObjsFilterWaiting.count(), 1)
		self.assertEqual(allObjsFilterWaiting[0].title, 'sample title waiting')
		self.assertEqual(allObjsFilterWaiting[0].summary, 'sample summary waiting')
		self.assertEqual(allObjsFilterWaiting[0].status, 1)
		
		allObjsFilterFinished = savedTodos.filter(status=2)
		self.assertEqual(allObjsFilterFinished.count(), 1)
		self.assertEqual(allObjsFilterFinished[0].title, 'sample title finished')
		self.assertEqual(allObjsFilterFinished[0].summary, 'sample summary finished')
		self.assertEqual(allObjsFilterFinished[0].status, 2)
		
		allObjsFilterCancelled = savedTodos.filter(status=3)
		self.assertEqual(allObjsFilterCancelled.count(), 1)
		self.assertEqual(allObjsFilterCancelled[0].title, 'sample title cancelled')
		self.assertEqual(allObjsFilterCancelled[0].summary, 'sample summary cancelled')
		self.assertEqual(allObjsFilterCancelled[0].status, 3)
		
	def test_saving_and_retrieving_todos_with_date_filter(self):
		#tests listing of all todos regardless of the type
		#first create records, specifically three of them (from dec 21, dec 22, dec 23)
		
		form1 = Todo()
		form1.title = 'sample title waiting'
		form1.summary = 'sample summary waiting'
		form1.date = '2014-12-21'
		form1.status = 1
		form1.save()
		
		form2 = Todo()
		form2.title = 'sample title finished'
		form2.summary = 'sample summary finished'
		form2.date = '2014-12-22'
		form2.status = 2
		form2.save()
		
		form3 = Todo()
		form3.title = 'sample title cancelled'
		form3.summary = 'sample summary cancelled'
		form3.date = '2014-12-23'
		form3.status = 3
		form3.save()
		
		savedTodos = Todo.objects.all()
		
		#we want to get only betweeb dec 22 and dec 23
		dfrom = '20141222'
		dto = '20141223'
		savedTodos = savedTodos.filter(date__range=[ datetime.strptime(dfrom, '%Y%m%d' ),datetime.strptime(dto, '%Y%m%d' )])

		self.assertEqual(savedTodos.count(), 2)
		self.assertEqual(savedTodos[0].title, 'sample title finished')
		self.assertEqual(savedTodos[0].summary, 'sample summary finished')
		self.assertEqual(savedTodos[0].status, 2)
		self.assertEqual(savedTodos[1].title, 'sample title cancelled')
		self.assertEqual(savedTodos[1].summary, 'sample summary cancelled')
		self.assertEqual(savedTodos[1].status, 3)
		
	def test_saving_and_retrieving_with_after_date_modification(self):
		#tests listing of todos
		#modifies dates of all waiting todos that are before today
		#first create records, specifically three of them (from dec 21, dec 22, dec 23)
		#create 3 waiting todos
		form1 = Todo()
		form1.title = 'sample title one'
		form1.summary = 'sample summary one'
		form1.date = '2014-12-21'
		form1.status = 1
		form1.save()
		
		form2 = Todo()
		form2.title = 'sample title two'
		form2.summary = 'sample summary two'
		form2.date = '2014-12-22'
		form2.status = 1
		form2.save()
		
		form3 = Todo()
		form3.title = 'sample title three'
		form3.summary = 'sample summary three'
		form3.date = '2014-12-23'
		form3.status = 1
		form3.save()
		
		savedTodos = Todo.objects.all()
		
		#consider if today is dec 22
		today = datetime.strptime('20141222', '%Y%m%d' )
		#update all waiting todos date that are before today to today
		savedTodos.filter(status=1).filter(date__lt=today).update(date=today)

		self.assertEqual(savedTodos.count(), 3)
		#make sure this is the right entry we are checking by doing these asserts
		self.assertEqual(savedTodos[0].title, 'sample title one')
		self.assertEqual(savedTodos[0].summary, 'sample summary one')
		self.assertEqual(savedTodos[0].status, 1)
		#its date should be converted to dec 22, check if that is the case
		self.assertEqual(savedTodos[0].date.strftime('%Y%m%d'), '20141222')
