from selenium import webdriver
from selenium.webdriver.common.by import By  # Import module By untuk mencari elemen berdasarkan atribut
from selenium.webdriver.support import expected_conditions as EC

import time
import ait #for automating windows explorer
import os

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"')
driver = webdriver.Chrome(chrome_options)

def login_mobile(username, password):
    driver.get('https://www.instagram.com')
    time.sleep(5)
    driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')[0].click()
    time.sleep(5)
    driver.find_element_by_name('username').send_keys(username) 
    driver.find_element_by_name('password').send_keys(password) 
    driver.find_elements_by_xpath("//div[contains(text(), 'Log in')]")[0].click()
    time.sleep(10)
    driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button')[0].click()
    time.sleep(5)
    try:
        driver.find_elements_by_xpath("//button[contains(text(), 'Abbrechen')]")[0].click()
    except:
        print('errorcode=1')
        pass

def login_pc(username, password):
    driver.get('https://www.instagram.com')
    time.sleep(15)
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH,"//div[contains(text(), 'Log in')]").click()
    time.sleep(15)
    print('logged in successfully')


def Upload(file_name, caption, caption_status, resize_status):
    absolute_file_path = os.path.abspath(__file__)[:-12] + 'media\\unposted\\' + file_name
    print(absolute_file_path)
    driver.get('https://www.instagram.com/')
    time.sleep(5)
    driver.find_element("//span[contains(text(),'Create')]").click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()
    time.sleep(1.5)
    ait.win_active("Öffnen") 
    time.sleep(2)
    ait.control_send("Öffnen","Edit1",absolute_file_path) 
    time.sleep(1.5)
    ait.control_send("Öffnen","Edit1","{ENTER}")
    time.sleep(10)


    if bool(resize_status) == True:
        print(bool(resize_status))
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]').click()
        time.sleep(1)
        '//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]'
        '//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span'
        '//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]'
        print('Resized')
    else:
        print('Not resized')


    driver.find_element_by_xpath("//button[contains(text(),'Weiter')]").click()

    time.sleep(1.5)
    print(caption_status)

    if bool(caption_status) == True:

        driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').send_keys(caption)
        driver.find_element_by_xpath("//button[contains(text(),'Teilen')]").click()
        print('posted sucessfully.')
        print('caption: ' + caption)

    else:

        driver.find_element_by_xpath("//button[contains(text(),'Teilen')]").click()
        print('posted sucessfully.')
        print('caption: none')
