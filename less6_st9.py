from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("form-control.first")
    input1.send_keys("Yasuro")
    input2 = browser.find_element_by_class_name("form-control.second")
    input2.send_keys("Kabo")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("bubabuba")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(20)
    browser.quit()
