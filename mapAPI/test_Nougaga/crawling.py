from selenium import webdriver as wd
driver = wd.Chrome(executable_path='chromedriver.exe')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('http://')

driver.find_elements_by_css_selector().