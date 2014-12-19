from selenium import webdriver
import unittest

class RegistrationTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_go_to_homepage_and_register(self):
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
		
		login_link = self.browser.find_element_by_link_text('here')
		login_link.click()
		
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
		
		# He is greeted with a note "Hi John!"
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Hi John Laput!', body.text)

		# He is then decided to logout for now and sleep
		logout_link = self.browser.find_element_by_link_text('Logout')
		logout_link.click()
		
		#checked if loggedout
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('You are now logged out', body.text)
		
		#self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')