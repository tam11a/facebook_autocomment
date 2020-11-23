#---------Built-in Modules----
import json
from random import choice
from time import sleep, time
#-----------------------------
#---------3rd Party Modules---
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#-----------------------------

class Client:
    def __init__(self, username, password, browser='chrome', isHeadless=True, Notifications=False):
        
        self.username = username
        self.password = password
        
        try:
            if browser.lower() == 'chrome':
                from selenium.webdriver.chrome.options import Options
            elif browser.lower() == 'firefox':
                from selenium.webdriver.firefox.options import Options
            
            chrome_options = Options() 

            if isHeadless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-sh-usage")
            chrome_options.add_argument('--log-level=3')
            chrome_options.add_argument('--disable-extensions')
            if not Notifications:
                if browser.lower() == 'chrome':
                    prefs = {"profile.default_content_setting_values.notifications" : 2}
                    chrome_options.add_experimental_option("prefs",prefs)
                elif browser.lower() == 'firefox':
                    chrome_options.set_preference("dom.push.enabled", False)
            if browser.lower() == 'chrome':
                self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'drivers\chromedriver')
            elif browser.lower() == 'firefox':
                self.browser = webdriver.Firefox(options=chrome_options, executable_path=r'drivers\geckodriver')
        except Exception as e:
            print(e)
        else:
            #self.browser.get("http://m.facebook.com")
            self.browser.get("https://m.facebook.com/login.php?")
            self.Login()
    
    def Login(self, username = None, password = None):
        
        username = self.username
        password = self.password
    
        try:
            e_username = self.browser.find_element_by_id("m_login_email")
            e_password = self.browser.find_element_by_id("m_login_password")
            e_button = self.browser.find_element_by_id("u_0_4")
        except Exception as error:
            print(error)
        else:                
            e_username.send_keys(username)
            print(username+" is logging in.....")
            e_password.send_keys(password)
            e_button.click()
                
        tryRound = 1
        while tryRound:
            lap = 20
            while lap:
                if self.browser.current_url == "https://m.facebook.com/login/save-device/?login_source=login#_=_" or self.browser.current_url == "https://m.facebook.com/checkpoint/?__req=b":
                    break
                else:
                    sleep(1)
                    lap -= 1
            
            if lap:
                #print("Passed!")
                if self.browser.current_url == "https://m.facebook.com/checkpoint/?__req=b":

                    approvals_code = self.browser.find_element_by_id("approvals_code")
                    approvals_btn  = self.browser.find_element_by_id("checkpointSubmitButton-actual-button")
                    oop = 0
                    while self.browser.current_url != "https://m.facebook.com/login/checkpoint/":
                        if oop:
                            print("Wrong 2fa Code.")
                        else: 
                            oop += 1
                        approvals_code.send_keys(self.on2fa())
                        approvals_btn.click()
                        print("Submitting Code...")
                    
                    print("Saving Browser..")
                    approvals_btn  = self.browser.find_element_by_id("checkpointSubmitButton-actual-button")
                    approvals_btn.click()
                    print("Browser Saved.")
                print("Login Successful...!!")
                #self.Open("http://m.facebook.com")
                tryRound = 0
            else:
                line = ""
                try:
                    if self.browser.find_element_by_id("login_error").text:
                        
                        line = "The mobile number or email address that you've entered doesn't match any account."
                        tryRound = 0
                    else:

                        line = "Unstable or Slow Internet Connection."
                    print()
                    print("Try #"+str(tryRound)+":")
                    print(line)
                    tryRound += 1
                except:
                    self.Open("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8")
                    return self.Login()
            
    
    def on2fa(self):
        return input("Enter 2fa Code -->")

    def Open(self, link="http://m.facebook.com"):
        print('Opening ', end='')
        print(link)
        sleep(1)
        self.browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        self.browser.get(link)

    def Comment(self, link, text):
        link = link.replace("/www.", "/m.")
        self.Open(link)
        sleep(0.5)
        
        try:
            commentbox = self.browser.find_element_by_id("composerInput")
        
        except:
            sleep(0.5)
            print("Retrying.....")
            self.Comment(link, text)
        else:
            commentbox.send_keys(text)
            sleep(1)
            commentbox.submit()
            print("[$Comment Delivered to a Post at "+str(time())+"]")
    
    def Close(self):
        self.browser.close()

    def getURL(self):
        return self.browser.current_url
    
    def Alert(self, Accept=False):
        if Accept:
            self.browser.switch_to.alert.accept()
        else:
            self.browser.switch_to.alert.dismiss()
    
    def commentInFlow(self, url=None, comments=[], num=1):
        try:
            for i in range(int(num)):
                self.Comment(url, choice(comments))
                sleep(choice([0.5, 0.6, 0.55, 1.0]))
        except Exception as e:
            print(e)
        else:
            print("[$Comments("+str(num)+") Delivered]")
