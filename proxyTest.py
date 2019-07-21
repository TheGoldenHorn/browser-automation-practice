import os, json, time, socket, random, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *


myProxy= ["34.248.190.13", "34.250.207.122", "34.248.190.13",  "34.249.24.49"] 
myHost = "3128"
end= int(len(myProxy)) +1
for i in range(0,end):
	profile = webdriver.FirefoxProfile()
	profile.set_preference('network.proxy.ftp', myProxy[i])
	profile.set_preference('network.proxy.ftp_port', int(myHost))
	profile.set_preference("network.proxy.type", int('1')) 
	profile.set_preference("network.proxy.http", myProxy[i])
	profile.set_preference("network.proxy.http_port", int(myHost))
	profile.set_preference("network.proxy.ssl", myProxy[i])
	profile.set_preference("network.proxy.ssl_port", int(myHost))
	profile.set_preference("network.proxy.socks", myProxy[i])
	profile.set_preference("network.proxy.socks_port", int(myHost))
	profile.set_preference("network.proxy.share_proxy_settings",bool('True')) 
	profile.set_preference("network.cookie.prefsMigrated",bool('True'))
	profile.set_preference('signon.autologin.proxy', bool('True'))
	profile.set_preference('network.websocket.enabled', bool('False'))

	#profile.add_extension('closeproxy.xpi')
	##profile.set_preference('network.automatic-ntlm-auth.trusted-uris', 'myProxy')
	#credentials = '{user}:{pass}'.format(**proxy)
	#credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
	#profile.set_preference('extensions.closeproxyauth.authtoken', credentials)
	#profile.update_preferences()
	browser = webdriver.Firefox(profile)
	try:
				

		browser.implicitly_wait(10)
		browser.get('http://whatismyipaddress.com/')
		
		time.sleep(6)
		browser.quit()
		#myProxy = "13.54.126.232:3128"

		'''proxy = Proxy({
			'proxyType': ProxyType.MANUAL,
			'httpProxy': myProxy,
			'ftpProxy': myProxy,
			'sslProxy': myProxy,
			'noProxy': myProxy # set this value as desired
			})
		'''
		#driver = webdriver.Firefox(proxy=proxy)
		#driver.get("http://www.google.com")
		#raw_input() .

		raw_input()
	except Exception as e:
		browser.quit()
		print e
		pass