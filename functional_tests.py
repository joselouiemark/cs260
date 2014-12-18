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
		self.fail('Finish the test!')
		
		# He is invited to login or create an account

		# He filled up the form
		# He typed "johnlaput" on the user name text box
		# He typed "John" on the first name text box
		# He typed "Laput" on the last name text box
		# He typed "johnlaput@gmail.com" on the email text box
		# He typed "pwd123" on the password text box
		# He typed "pwd123" on the retype password text box

		# He is then redirected to the homepage and invited again to login or create an account

		# He logs in using "johnlaput" as username and "pwd123" as password

		# He then is redirected to the main dashboard where there is a list of to-do things, which is empty for now
		# He is greeted with a note "Hi John!"

		# He is then decided to logout for now and sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')