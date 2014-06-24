from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
### function definitions
def measureTimeToAddMany(exampleName, driver):
	try :
		WebElement = driver.find_element_by_id("new-todo")
	except : #Any exception! Want WebElement is None at least, but that doesn't trigger as I expected, and misses when the page isn't returned
		print exampleName+": doesn't return a page, or doesn't have the expected new-todo element available on the page"
		return()
	startTime = time.time()
	addMany( WebElement )
	endTime = time.time()
	print exampleName+": "+str(endTime - startTime)

def addMany( WebElement ):
	for x in range(0,numberOfItemsToAdd):
		try :
			WebElement.send_keys("somestuff"+str(x));
			WebElement.send_keys(Keys.RETURN);
		except:
			print("can't send keyboard input!")

def processSet(name, examples, root):
	print(name)
	for thing in examples:
		driver.get(root+thing+"/")	
		measureTimeToAddMany(thing, driver)

def getDriver(desiredDriver):
	if (desiredDriver == "chrome") :
		print("using Chrome")
		return(webdriver.Chrome("./chromedriver"))
	print("using Firefox by default")
	return(webdriver.Firefox())

def makeURL(directory):
	return(firstPartUrl+directory+"/")

def setUpExamples():
	## set up data (notes for those which can't be done in this way...)
	#
	global architectureExamples	, dependencyExamples , vanillaExamples , labsArchitectureExamples , labsDependencyExamples
	#
	architectureExamples = ('agilityjs', 'angularjs', 'angularjs-perf', 'backbone', 'canjs', 'closure', 'dojo', 'emberjs', 'gwt', 'jquery', 'knockback', 'knockoutjs', 'maria', 'polymer', 'react', 'spine', 'yui')
	## can't do polymer
	#
	dependencyExamples = ('backbone_require', 'emberjs_require', 'flight')
	## emberjs_require no longer exists
	#
	vanillaExamples = ('vanilladart/web', 'vanillajs')
	## note odd end on vanilladart
	#
	labsArchitectureExamples = ('angular-dart/web', 'atmajs', 'backbone_marionette', 'dijon', 'duel/www', 'epitome', 'exoskeleton', 'firebase-angular', 'kendo', 'mozart', 'olives', 'plastronjs', 'puremvc', 'ractive', 'react-backbone', 'sammyjs', 'serenadejs', 'somajs', 'stapes', 'typescript-angular', 'typescript-backbone', 'vue', 'ariatemplates',  'batman', 'componentjs', 'cujo', 'derby', 'extjs_deftjs', 'meteor', 'montage', 'polymer', 'rappidjs', 'sapui5', 'socketstream', 'thorax')
	## error for socketstream is unhandled
	## can't do 'ariatemplates',  'batman' (*OK on 3, not OK on 100), 'componentjs', 'cujo', 'derby', 'extjs_deftjs', 'meteor', 'montage', 'polymer', 'rappidjs', 'sapui5', 'socketstream', 'thorax',
	#
	labsDependencyExamples = ('angularjs_require', 'enyo_backbone', 'flight', 'knockoutjs_require', 'somajs_require', 'stapes_require', 'troopjs_require', 'backbone_marionette_require', 'canjs_require', 'chaplin-brunch', 'durandal', 'lavaca_require', 'thorax_lumbar/public')
	# can't do 'backbone_marionette_require', 'canjs_require', 'chaplin-brunch', 'durandal', 'lavaca_require', 'thorax_lumbar/public',
###

####################################################################
## body starts here
numberOfItemsToAdd = 2
targetBrowser = "chrome"
firstPartUrl = "http://0.0.0.0/todomvc/"
setUpExamples()

# kick off Selenium
driver = getDriver(targetBrowser)
# give the 5 sets of examples and their relevant paths to the processor
processSet("stable architecture examples", architectureExamples, makeURL("architecture-examples") )
processSet("stable dependency examples", dependencyExamples, makeURL("dependency-examples/" ) )
processSet("stable vanilla examples", vanillaExamples, makeURL("vanilla-examples/" ) )
processSet("labs architecture examples", labsArchitectureExamples, makeURL("labs/architecture-examples/" ) )
processSet("labs dependency examples", labsDependencyExamples, makeURL("labs/dependency-examples/" ) )
