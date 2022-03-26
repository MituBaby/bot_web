from lib2to3.pgen2 import driver
from selenium import webdriver

a = webdriver.Chrome()

a.get("https://student.amikompurwokerto.ac.id/auth")
a.find_element_by_xpath('//*[@id="exampleInputEmail1"]').send_keys("21SA3085")
a.find_element_by_xpath('//*[@id="exampleInputPassword1"]').send_keys("12503")
a.find_element_by_css_selector(
    '#login-form > div > div:nth-child(6) > button').click()
a.get("https://student.amikompurwokerto.ac.id/Main")
a.get("https://student.amikompurwokerto.ac.id/presensi")
a.find_element_by_css_selector('#thn_akademik').click()
a.find_element_by_css_selector('#thn_akademik > option').click()
a.find_element_by_css_selector('#semester').click()
