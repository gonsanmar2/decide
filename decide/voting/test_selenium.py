# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestVotingTestCase():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_votingTestCase(self):
    self.driver.get("http://localhost:8080/booth/4/")
    self.driver.set_window_size(1296, 704)
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("pruebaSelenium")
    self.driver.find_element(By.ID, "password").send_keys("decide2023")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(4) > .form-group").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(4) > .form-group").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(4) > .form-group").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(4) > .form-group")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "q3").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()