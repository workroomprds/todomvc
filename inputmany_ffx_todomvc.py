from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
frameworks = ['backbone', 'angularjs', 'angularjs-perf', 'emberjs', 'knockoutjs', 'dojo', 'yui', 'agilityjs']
driver = webdriver.Firefox()
for thing in frameworks:
	driver.get("http://0.0.0.0/todomvc/architecture-examples/"+thing+"/")
	WebElement = driver.find_element_by_id("new-todo")
	startTime = time.time()
	for x in range(0,299):
		WebElement.send_keys("somestuff"+str(x));
		WebElement.send_keys(Keys.RETURN);
	endTime = time.time()
	print thing+": "+str(endTime - startTime)
