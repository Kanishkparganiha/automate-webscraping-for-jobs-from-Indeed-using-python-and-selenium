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

time.sleep(2)


login_payload={'email':'*****@gmail.com','password':'*******'}

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
Location.send_keys(Keys.RETURN)

time.sleep(3)

#browser.find_element_by_xpath('//button[normalize-space()="Find jobs"]').click()

time.sleep(2)
browser.execute_script("window.scrollTo(0, 9000)")

job_title=[i.text for i in browser.find_elements_by_xpath('//td[@class="resultContent"]')]
company=[i.text for i in browser.find_elements_by_xpath('//div[@class="heading6 company_location tapItem-gutter"]')]
links=[i.get_attribute('href') for i in browser.find_elements_by_xpath('//a[@rel="nofollow" and @data-hide-spinner="true"]')]




############## Under Developement

time.sleep(2)
browser.execute_script("window.scrollTo(0, 9000)")

page=2
try:
    pass
    while page<6:
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 9000)")
        print('Extracting from page %s'%page)
        webpage='//a[@aria-label="%s"]'%(page)
        browser.find_element_by_xpath(webpage).click()
        time.sleep(3)

        job_title+=[i.text for i in browser.find_elements_by_xpath('//td[@class="resultContent"]')]
        time.sleep(2)
        company+=[i.text for i in browser.find_elements_by_xpath('//div[@class="heading6 company_location tapItem-gutter"]')]
        time.sleep(2)
        links+=[i.get_attribute('href') for i in browser.find_elements_by_xpath('//a[@rel="nofollow" and @data-hide-spinner="true"]')]



        page+=1



except Exception as e:
    print(e)
    browser.refresh()


print('Finished Extracting')




df=pd.DataFrame({'Job':job_title,'Company':company,'Link':links})
import re

##df=pd.DataFrame({'Company':company,'Link':links})





def regex(txt):
    txt=re.sub('\n',' ',txt)
    return txt

df['Job']=df['Job'].apply(lambda x:regex(x))
df['Company']=df['Company'].apply(lambda x:regex(x))
df.index=range(1,len(df)+1)



def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

# link is the column with hyperlinks
df['Link'] = df['Link'].apply(make_clickable)
df.to_html('~/data_science/PythonCode/Indeed.html',escape=False)
