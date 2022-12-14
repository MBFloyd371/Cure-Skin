from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.events import EventFiringWebDriver
#from support.logger import logger, MyListener

from app.application import Application




# Allure command:
#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/sign-in.feature

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\mbflo\Automation\Cure-Skin\chromedriver.exe')
    # webdriver.Edge(executable_path=r'C:\Users\mbflo\selenium\msedgedriver.exe')
    # webdriver.Chrome(executable_path=r'C:\Users\mbflo\Automation\python-selenium-automation\chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     executable_path=r'C:\Users\mbflo\Automation\Cure-Skin\chromedriver.exe'
    # )

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    #context.driver = EventFiringWebDriver(
         #webdriver.Chrome(
             #executable_path=r'C:\Users\mbflo\Automation\Cure-Skin\chromedriver.exe'
         #),
         #MyListener())
    # for headless mode ###
    #context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    ###for browerstack ###
    #desired_cap = {
        #'browser': 'Chrome',
         #'os_version': '11',
         #'os': 'Windows',
         #'name': test_name
    #}
    #bs_user = 'marcusfloyd_YqUcLk'
    #bs_key = 'zRhMbAEy2EV5PfF4MenL'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)



    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    #logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        #logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()