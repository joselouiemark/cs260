from selenium import webdriver
import unittest

class RegistrationTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
		
	def do_register(self):
		# John wants to organize his activities for each day. Goes to the scheduler app homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention Scheduler
		self.assertIn('To-Do', self.browser.title)
		
		# He is invited to login or create an account
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('User name:', body.text)
		self.assertIn('Password:', body.text)
		
		# He clicked register
		reg_link = self.browser.find_element_by_link_text('Register')
		reg_link.click()
		
		# Reset browser
		body = self.browser.find_element_by_tag_name('body')
		# Make sure that we are in registration page
		self.assertIn('Username', body.text)
		self.assertIn('First Name', body.text)
		self.assertIn('Last Name', body.text)
		self.assertIn('Email', body.text)
		self.assertIn('Password', body.text)
		
		
		# He filled up the form
		# He typed "johnlaput" on the user name text box
		self.browser.find_element_by_name('username').send_keys("johnlaput")
		# He typed "John" on the first name text box
		self.browser.find_element_by_name('first_name').send_keys("John")
		# He typed "Laput" on the last name text box
		self.browser.find_element_by_name('last_name').send_keys("Laput")
		# He typed "johnlaput@gmail.com" on the email text box
		self.browser.find_element_by_name('email').send_keys("johnlaput@gmail.com")
		# He typed "pwd123" on the password text box
		self.browser.find_element_by_name('password1').send_keys("pwd123")
		# He typed "pwd123" on the retype password text box
		self.browser.find_element_by_name('password2').send_keys("pwd123")
		self.browser.implicitly_wait(3)
		# John clicks the save button
		self.browser.find_element_by_css_selector("input[value='register']").click()
		
		# Goes to the registration confirmation page and is registered
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('You have registered', body.text)
	
	def do_login(self):
		self.browser.get('http://localhost:8000/accounts/login/')
		
		# He is then redirected to the homepage and invited again to login or create an account
		# Reset browser
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('User name:', body.text)
		self.assertIn('Password:', body.text)
		
		# He logs in using "johnlaput" as username and "pwd123" as password
		self.browser.find_element_by_name('username').send_keys("johnlaput")
		self.browser.find_element_by_name('password').send_keys("pwd123")
		self.browser.implicitly_wait(3)
		
		# user clicks the save button
		self.browser.find_element_by_css_selector("input[value='login']").click()
		
		# He then is redirected to the main dashboard where there is a list of to-do things, which is empty for now
		self.assertIn('TODO', self.browser.title)
	
	def do_logout(self):
		self.browser.get('http://localhost:8000')
		
		# He is then decided to logout for now and sleep
		logout_link = self.browser.find_element_by_link_text('Logout')
		logout_link.click()
		
		#checked if loggedout
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('You are now logged out', body.text)
		
	def do_add_item(self,ititle,isummary,idate,istatus):
		self.browser.get('http://localhost:8000')
		reg_link = self.browser.find_element_by_link_text('Add Item')
		reg_link.click()
	
		self.browser.find_element_by_name('title').send_keys(ititle)
		self.browser.find_element_by_name('summary').send_keys(isummary)
		self.browser.find_element_by_name('date').send_keys(idate)
		self.browser.find_element_by_name('status').send_keys(istatus)
		
		self.browser.find_element_by_css_selector("input[value='save']").click()
	
	def test_a_register_login_view_listarticles_and_logout(self):
		#user register
		self.do_register()
		
		login_link = self.browser.find_element_by_link_text('here')
		login_link.click()
		
		#user login
		self.do_login()
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		self.do_logout()
		
	def test_b_item_add(self):
		#user login
		self.do_login()
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		# Seeing he don't have any todo items he decided to add
		# Added "eat at jollibee" todo
		self.do_add_item('Eat at Jollibee','Eat fries and burger',"2014-12-25",1)
		self.do_add_item('Buy shoes','Nike air or Jordan brand',"2014-12-25",1)
		self.do_add_item('Cut hair','Army cut',"2014-12-26",1)
		self.do_add_item('Walk the doc','Three times around the park',"2014-12-27",1)
		
		self.browser.get('http://localhost:8000')
		
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Eat at Jollibee', body.text)
		self.assertIn('Buy shoes', body.text)
		self.assertIn('Cut hair', body.text)
		self.assertIn('Walk the doc', body.text)
		
		# He decided to logout
		self.do_logout()
		
	def test_c_adjust_time(self):
		#user login
		self.do_login()
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		# Seeing he don't have any todo items he decided to add
		# Added "eat at jollibee" todo
		self.do_add_item('Eat at Jollibee','Eat fries and burger',"2014-11-01",1)
		self.do_add_item('Buy shoes','Nike air or Jordan brand',"2014-12-01",1)
		self.do_add_item('Cut hair','Army cut',"2014-11-02",1)
		self.do_add_item('Walk the doc','Three times around the park',"2013-11-01",1)
		
		self.browser.get('http://localhost:8000')
		
		body = self.browser.find_element_by_tag_name('body')
		self.assertNotIn('2014-11-01', body.text)
		self.assertNotIn('2014-12-01', body.text)
		self.assertNotIn('2014-11-02', body.text)
		self.assertNotIn('2013-11-01', body.text)
		
		# He decided to logout
		self.do_logout()
		
	
	def test_d_edit_item_to_done(self):
		#user login
		self.do_login()
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		# Seeing he don't have any todo items he decided to add
		# Added "eat at jollibee" todo
		self.do_add_item('Eat at Jollibee','Eat fries and burger',"2014-11-01",1)
		
		# He was done
		self.browser.get('http://localhost:8000')
		logout_link = self.browser.find_element_by_link_text('Finish')
		logout_link.click()
		
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Done', body.text)
		
		# He decided to logout
		self.do_logout()
		
	def test_e_edit_item_to_cancelled(self):
		#user login
		self.do_login()
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		# Seeing he don't have any todo items he decided to add
		# Added "eat at jollibee" todo
		self.do_add_item('Eat at Jollibee','Eat fries and burger',"2014-11-01",1)
		
		# He has no money thus decided to cancel
		self.browser.get('http://localhost:8000')
		logout_link = self.browser.find_element_by_link_text('Cancel')
		logout_link.click()
		
		body = self.browser.find_element_by_tag_name('body')
		self.assertNotIn('Cancelled', body.text)
		
		# He decided to logout
		self.do_logout()
		
	def test_e_edit_item_edit_date_title_and_summary(self):
		#user login
		self.do_login()
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		# Seeing he don't have any todo items he decided to add
		# Added "eat at jollibee" todo
		self.do_add_item('Eat at Jollibee','Eat fries and burger',"2014-11-01",1)
		
		# He clicked title to view and edit todo
		self.browser.get('http://localhost:8000')
		logout_link = self.browser.find_element_by_link_text('Eat at Jollibee')
		logout_link.click()
		
		# He decided to go to McDonald's instead
		self.browser.find_element_by_name('title').send_keys('Eat at mcdo')
		# Get McFloat instead
		self.browser.find_element_by_name('summary').send_keys('McFloat and Fries')
		# Go next year on his birthday instead
		self.browser.find_element_by_name('date').send_keys('2015-02-01')
		
		self.browser.find_element_by_css_selector("input[value='save']").click()
		
		self.browser.get('http://localhost:8000')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Eat at mcdo', body.text)
		self.assertIn('McFloat and Fries', body.text)
		self.assertIn('2015-02-01', body.text)
		
		# He decided to logout
		self.do_logout()

if __name__ == '__main__':
	unittest.main(warnings='ignore')