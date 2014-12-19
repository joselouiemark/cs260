from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from todolists.views import home_page
from cs260.views import login

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
	
	def test_login_page_returns_correct_html(self):
		request = HttpRequest()
		response = login(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>Login</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
	
	def test_register_returns_correct_html(self):
		request = HttpRequest()
		response = login(request)
		self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
		self.assertIn(b'<title>Register</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
	
	def test_register_can_save_a_user_registration(self):
		request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

		
		
		
		
