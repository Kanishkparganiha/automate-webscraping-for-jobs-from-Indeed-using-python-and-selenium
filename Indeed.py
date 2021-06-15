from selenium import webdriver
from bs4 import BeautifulSoup
import time
browser = webdriver.Chrome(executable_path=r'/home/kanishka/Downloads/chromedriver')
import itertools
import pandas as pd
from selenium.webdriver.common.keys import Keys


#url='https://www.raisegreen.com/blog'
url='https://secure.indeed.com/account/login?hl=en_US&service=my&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F'
#url=input("Enter the URL of the webpage: ")

browser.get(url)



login_payload={'email':'parganiha.k@northeastern.edu','password':'Tenda@220'}

username=browser.find_elements_by_xpath('//input[@id="login-email-input"]')[0]
username.send_keys(login_payload['email'])

username=browser.find_elements_by_xpath('//input[@id="login-password-input"]')[0]
username.send_keys(login_payload['password'])

browser.find_elements_by_xpath('//button[@id="login-submit-button"]')[0].click()

payload={'Job':'Data Scientist','Location':'United States'}

Job=browser.find_elements_by_xpath('//input[@id="text-input-what"]')[0]
Job.send_keys(payload['Job'])

Location=browser.find_elements_by_xpath('//input[@id="text-input-where"]')[0]
Location.send_keys(Keys.CONTROL, 'a')
Location.send_keys(Keys.BACKSPACE)

Location.send_keys(payload['Location'])

time.sleep(2)

browser.find_element_by_xpath('//button[normalize-space()="Find jobs"]').click()

job_title=[i.find_element_by_tag_name('h2').text for i in browser.find_elements_by_xpath('//div[@class="slider_container"]')]
company=[i.text for i in browser.find_elements_by_xpath('//div[@class="heading6 company_location tapItem-gutter"]')]
links=[i.get_attribute('href') for i in browser.find_elements_by_xpath('//a[@rel="nofollow" and @data-hide-spinner="true"]')]


page=input('Enter page no:')
webpage='//a[@aria-label="%s"]'%(page)
browser.find_element_by_xpath(webpage).click()




df=pd.DataFrame({'Job':job_title,'Company':company,'Link':links})


import re

def regex(txt):
    txt=re.sub('\n',' ',txt)
    return txt

df['Job']=df['Job'].apply(lambda x:regex(x))
df['Company']=df['Company'].apply(lambda x:regex(x))


############## Under Developement


page=2
try:
    pass
    while page<6:
        time.sleep(2)
        print('Extracting from page %s'%page)
        webpage='//a[@aria-label="%s"]'%(page)
        browser.find_element_by_xpath(webpage).click()
        time.sleep(3)

        job_title+=[i.find_element_by_tag_name('h2').text for i in browser.find_elements_by_xpath('//div[@class="slider_container"]')]
        company+=[i.text for i in browser.find_elements_by_xpath('//div[@class="heading6 company_location tapItem-gutter"]')]
        links+=[i.get_attribute('href') for i in browser.find_elements_by_xpath('//a[@rel="nofollow" and @data-hide-spinner="true"]')]



        page+=1



except Exception as e:
    print(e)
    browser.refresh()

print('Finished Extracting')

df.to_csv('Indeed.csv')
