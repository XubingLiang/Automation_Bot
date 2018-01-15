from selenium import webdriver
import selenium
import time


#20172892 flower9see
class automatic_online_study():

	def __init__(self, username, password,week):
		print "initilising the browser"
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('headless')
		self.options.add_argument('window-size=2560x1600')
		self.username = username
		self.password=password
		self.week=week

	def login(self):
		print "start logining"
		self.driver = webdriver.Chrome(chrome_options=self.options)
		self.driver.get('https://www.idealcol.com.au')
		print(self.driver.title)
		self.driver.find_element_by_id('username').send_keys(self.username)
		self.driver.find_element_by_id('password').send_keys(self.password)
		btn = self.driver.find_element_by_id("loginbtn")
		btn.click()

	def online_study(self):
		btn = self.driver.find_element_by_class_name("type_system")
		btn.click()
		print "study studying for week "+ str(self.week)
		text=content[str(self.week)]
		print(self.driver.title)
		print text
		if text == "2018T1-SYD PSPTIS060 (ADTC-F803)" or text == "2018T1-SYD PSPTIS067 (ADTC-F803)":
			text_arr=text.split(' ')
			study_content=text_arr[1]+"_Online Study Guide_Week "
			if text == "2018T1-SYD PSPTIS060 (ADTC-F803)":
				study_content = study_content + str(self.week-5)
			else:
				study_content = study_content + str(self.week-8)
			print study_content
			link = self.driver.find_element_by_partial_link_text(text)
			link.click()
			study_link = self.driver.find_element_by_partial_link_text(study_content)
			study_link.click()
			while True:
				print "In progress"
				self.driver.refresh()
				time.sleep(600)
			pass
		else :
			text_arr=text.split(' ')
			study_content=text_arr[1]+"_Online Study Guide"
			link = self.driver.find_element_by_partial_link_text(text)
			link.click()
			print study_content
			study_link = self.driver.find_element_by_partial_link_text(study_content)
			study_link.click()
			while True:
				print "In progress"
				self.driver.refresh()
				time.sleep(600)


content={
	"1":"2018T1-SYD PSPTIS101 (ADTC-F803)",
	"2":"2018T1-SYD PSPTIS100 (ADTC-F803)",
	"3":"2018T1-SYD PSPTIS069 (ADTC-F803)",
	"4":"2018T1-SYD SITXLAN005 (ADTC-F803)",
	"5":"2018T1-SYD PSPTIS002 (ADTC-F803)",
	"6":"2018T1-SYD PSPTIS060 (ADTC-F803)",
	"7":"2018T1-SYD PSPTIS060 (ADTC-F803)",
	"8":"2018T1-SYD PSPTIS060 (ADTC-F803)",
	"9":"2018T1-SYD PSPTIS067 (ADTC-F803)",
	"10":"2018T1-SYD PSPTIS067 (ADTC-F803)",
	"11":"2018T1-SYD PSPTIS067 (ADTC-F803)",


}
# dcap = dict()
# dcap["phantomjs.page.settings.userAgent"] = (
#      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
#      "(KHTML, like Gecko) Chrome/15.0.87")
username=raw_input("please enter username:").strip()
password=raw_input("password:").strip()
week=int(raw_input("which week you want to study for? eg: 1 : ").strip())

naati=automatic_online_study(username,password,week)
naati.login()
naati.online_study()




