#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
	'browser': 'Chrome',
	'browser_version': '51.0',
	'os': 'Windows',
	'os_version': '7',
	'resolution': '1280x1024',
	'deviceOrientation' : 'landscape',
	'wait_time' : '60'
}

# desired_cap['browserstack.local'] = True
desired_cap['acceptSslCerts'] = True

# desired_cap = DesiredCapabilities.CHROME
# desired_cap['chromeOptions'] = {}
# desired_cap['chromeOptions']['args'] = ['--disable-plugins']

# desired_cap['build'] = 'june'
# desired_cap['project'] = 'designs'

driver = webdriver.Remote(
	command_executor='http://[user:key]@hub.browserstack.com:80/wd/hub',
	desired_capabilities=desired_cap)

file = open("clients.csv", "r")
lines = file.readlines()
file.close()

for line in lines:
	words = line.split(",")
	clientid =  int(words[0])
	clientname = words[1]
	clienturl = "http://example.com/?clientid={}#".format(clientid)
	clientfilename = ".\screenshots\screenshot_{}.png".format(clientid)

	driver.get(clienturl)
	driver.save_screenshot(clientfilename)

driver.quit()