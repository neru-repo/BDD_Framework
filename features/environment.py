from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(r"/Users/vignesh/Downloads/chromedriver_mac_arm64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("detach", True)


def before_feature(context, feature):
    print("Chrome is being launched")
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.get("https://stage.electriphi.dev/login")
    context.driver.maximize_window()


def after_feature(context, feature):
    print("Chrome is being closed")
    context.driver.quit()

