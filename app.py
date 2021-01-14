#modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time

#global assignments

#-->driver variable assignments
chromedriver = 'chromedriver.exe'   #assign to webdriver path
os.environ['webdriver.chrome.driver'] = chromedriver #setting environment
driver = webdriver.Chrome(executable_path=chromedriver) #new webdriver instance

url_container = [ #--> contain links that we will use for our automation
    'https://randomtodolistgenerator.herokuapp.com/library',  #url for pulling tasks
    'https://todoist.com/users/showlogin'   #url for loging in todoist app
    ]

def TaskScraper():
    print('Starting automation...opening browser')  #test line
    driver.get(url_container[0])    #pull a list of tasks from the current url
    xpath = '//*[@class="flexbox task-title"]/div' #for access to random tasks title
    tasks = driver.find_elements_by_xpath(xpath)
    task_list = [ ] #will store decoded tasks titles
    for i in range(len(tasks)):
        task_list.append(tasks[i].text)  #decode the tasks titles to text
    print('Tasks has been extracted succesfully!')
    return task_list #return a list of tasks that has been extracted for new purposes

def Logger(email, password, data): #parameters: user, password, data
    alerts = [  #alerts that will be printed on shell/command line
        'Logging in ToDoist...',
        'Passing credentials...',
        'Logged!',
        'Writing tasks...',
        'Process finished succesfully!'
    ]
    print(alerts[0])
    driver.get(url_container[1])
    print(alerts[1])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)   #pass first function parameter
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password) #pass second function parameter
    driver.find_element_by_xpath('//*[@id="login_form"]/button').click()
    print(alerts[2],'\n', alerts[3])
    time.sleep(5)
    for element in data[:5]: #only takes 5 elements from the third parameter
        try: #the first action is to find an xpath for add new tasks
            driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div[1]/div/ul/li/button').click() #add-tasks button
            driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div/div/ul/li/form/div[1]/div[1]/div/div/div/div/div/div/div/span').send_keys(element)
            driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div/div/ul/li/form/div[1]/div[1]/div/div/div/div/div/div/div/span').send_keys(Keys.ENTER)
        except: #once in text chart, we need to find a new xpath because of the add-tasks button xpath has changed
            # wait = WebDriverWait(driver,10)
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="agenda_view"]/div/div/div/ul/li[4]/form/div[2]/button[1]')))
            #new add tasks button
            driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div/div/ul/li/form/div[1]/div[1]/div/div/div/div/div/div/div/span').send_keys(element)

            #submit the text 
            driver.find_element_by_xpath('//*[@id="agenda_view"]/div/div/div/ul/li/form/div[1]/div[1]/div/div/div/div/div/div/div/span').send_keys(Keys.ENTER)
            time.sleep(1)
    time.sleep(3)
    driver.quit() #close the browser
    print(alerts[-1])

Logger('mrracontacto@gmail.com','this_is_the_password',TaskScraper()) #execute the script








