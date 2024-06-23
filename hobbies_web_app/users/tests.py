# import time
# from django.test import TestCase
# from django.contrib import auth
# from django.test import LiveServerTestCase 
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import Select

# from django.urls import reverse
# from django.core.files import File
# from django.db import models
# from django.contrib.auth.models import User
# from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options

# # options = Options()
# # options.binary_location = "C:\\path\\to\\chrome.exe"    #chrome binary location specified here
# # options.add_argument("--start-maximized") #open Browser in maximized mode
# # options.add_argument("--no-sandbox") #bypass OS security model
# # options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option('useAutomationExtension', False)
# # driver = webdriver.Chrome(options=options, executable_path=r'C:\path\to\chromedriver.exe')
# # driver.get('http://google.com/')

# TEST_USERNAME = 'admin'
# TEST_PASSWORD = 'admin'
# # date = '2016-07-12'
# # hobbies = 'Basketball'

# class UserTestCase(TestCase):
#     @classmethod
#     def setUp(self):
#         '''checking we'''
#         user = User.objects.create(username=TEST_USERNAME)
#         user.set_password(TEST_PASSWORD)
#         user.save()


#     def test_users_count(self):
#         '''checking we have 1 user in test DB'''

#         n_users = User.objects.all().count()
#         self.assertEqual(n_users, 1)

#     def test_user_password(self):
#         '''check the password for admin is set using django authentication'''
#         user = auth.authenticate(username=TEST_USERNAME, password=TEST_PASSWORD)
#         self.assertIsNotNone(user)

# class HobbiesTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().tearDownClass()
#         cls.chrome = webdriver.Chrome()
#         cls.chrome.implicitly_wait(10)
#     @classmethod
#     def tearDownClass(cls):
#         cls.chrome.quit()
#         super().tearDownClass()

#     def test_login_and_signup(self):
#         try:
#             self._profile_page()
#             username = 'user'
#             password1 = 'password'
#             self._signup(username, password)
#             self._logout()
#             self._login(username, password)
#             self._editdob()
#             self._edithobbies()
#         finally:
#             self._close_all_new_windows()
            

#     def _profile_page(self):
#         self.chrome.get(self.live_server_url)
#         WebDriverWait(self.chrome, 2).until(lambda _: 'localhost' in self.chrome.current_url)

#     def _signup(self):
#         signup_path = reverse('survey:signup')
#         WebDriverWait(self.chrome, 2).until(lambda _: 'signup_path' in self.chrome.current_url)
        
#         username_elem = self.chrome.find_element_by_css_selector('#id_username')
#         username_elem.send_keys(username)
#         password_elem = self.chrome.find_element_by_css_selector('#id_password')
#         password_elem.send_keys(password)
        
#     def _logout(self):
#         logout_path = reverse('survey:logout')
#         self.chrome.gret(self.live_server_url + logout_path)
#         WebDriverWait(self.chrome, 2).until(
#             lambda _: self.live_server_irl + '/' == self.chrome.current_url
#         )


 
#     def _login(self, username, password):
#         signup_path = reverse('Hobbies:login')
#         self.chrome.get(self.live_server_url + signup_path)


#         password_elem = self.chrome.find_element_by_css_selector('#id_password')
#         password_elem.send_keys(password)

#         username_elem = self.chrome.find_element_by_css_selector('#id_username')
#         username_elem.send_keys(username)

#         signup_btn = self.chrome.find_element_by_css_selector('#')
#         signup_btn.click()
#         hobbies_path = reverse('hobby:hobbies')


#     class TestPersonCreationForm(TestCase):
#         def test_empty_form(self):
#             form = PersonCreationFormceForm()
#             self.assertInHTML(
#                 '<input type="text" name="dob" required id="dob">', str(form)
#             )
#             self.assertInHTML(
#                 '<input type="text" name="hobbies" required id="hobbies">', str(form)
#             )
#         def _edit(self):
#             request = HttpRequest()
#             request.PUT = {
#                 "dob": "2021-06-15",
#                 "hobbies": "Volleyball",
#             }

#         #form = PersonCreationForm(request.PUT, username=username)
