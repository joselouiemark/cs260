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
		self.assertIn('Username', body.text)
		self.assertIn('First Name', body.text)
		
		# He clicked register
		reg_link = self.browser.find_element_by_link_text('Register')
		home_link.click()
		
		# Reset browser
		# Make sure that we are in registration page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Username', body.text)
		self.assertIn('First Name', body.text)
		self.assertIn('Last Name', body.text)
		self.assertIn('Email', body.text)
		self.assertIn('Password', body.text)
		
		
		# He filled up the form
		self.browser.find_element_by_name('username').send_keys("louieano")
		self.browser.find_element_by_name('first_name').send_keys("louie")
		self.browser.find_element_by_name('last_name').send_keys("ano")
		self.browser.find_element_by_name('email').send_keys("louie@gmail.com")
		self.browser.find_element_by_name('password1').send_keys("louie123")
		self.browser.find_element_by_name('password2').send_keys("louie123")
		
		# He typed "johnlaput" on the user name text box
		# He typed "John" on the first name text box
		# He typed "Laput" on the last name text box
		# He typed "johnlaput@gmail.com" on the email text box
		# He typed "pwd123" on the password text box
		# He typed "pwd123" on the retype password text box

		# He is then redirected to the homepage and invited again to login or create an account

		# He logs in using "johnlaput" as username and "pwd123" as password

		self.browser.implicitly_wait(3)
		# He then is redirected to the main dashboard where there is a list of to-do things, which is empty for now
		# He is greeted with a note "Hi John!"

		# He is then decided to logout for now and sleep
		
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')