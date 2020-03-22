import os
import sys
from time import sleep
import creds as c
from selenium import webdriver
from selenium.webdriver.common import keys


class projectSync:
    def __init__(self, username, password):
        repo_name = input('Please input repo name: ')
        desc = input('Please input repo description: ')
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self.driver.get('https://github.com/')
        self.driver.find_element_by_xpath("//a[contains(@href,'/login')]").click()

        login_field= self.driver.find_element_by_id("login_field")
        pw_field = self.driver.find_element_by_id("password")
        sleep(1)
        login_field.clear()
        sleep(1)
        login_field.send_keys(self.username)
        sleep(.25)
        pw_field.clear()
        sleep(.38)
        pw_field.send_keys(self.password)
        sleep(.75)
        pw_field.send_keys(keys.Keys.RETURN)
        sleep(2.26)
        link = self.driver.find_element_by_class_name("dropdown-caret")
        sleep(.214)
        link.click()
        sleep(.380)
        create_new_repo= self.driver.find_element_by_xpath("//a[contains(@href,'/new')]")
        sleep(.60)
        create_new_repo.click()
        sleep(2)
        repo_name_field= self.driver.find_element_by_id('repository_name')
        sleep(.224)
        repo_name_field.send_keys(repo_name)
        sleep(.245)
        desc_field= self.driver.find_element_by_id('repository_description')
        desc_field.send_keys(desc)
        sleep(0.2158)
        visible= self.driver.find_element_by_id('repository_visibility_private')
        visible.click()
        sleep(.3568)
        repo_init = self.driver.find_element_by_id('repository_auto_init')
        repo_init.click()
        sleep(0.4485)
        self.driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[1]/details/summary/span').click()
        sleep(0.145)
        ignore_field= self.driver.find_element_by_id('context-ignore-filter-field')
        ignore_field.send_keys('Python')
        self.driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[1]/details/details-menu/div[3]/div[1]/label[86]/span').click()
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[3]/button").click()
        sleep(2)
       # can predict the git url because it is predictable
        #self.driver.close()
        rep_link = 'https://'+self.username+':'+c.token+'@github.com/sudhir22yadav/'+repo_name+'.git'
        self.driver.close()

        print(rep_link)
        '''
        repo_link_drop= self.driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div[3]/span/details/summary')
        repo_link_drop.click()
        '''
        clone = 'git clone '+ rep_link +' ~/github/'+repo_name+'/'
        repo_dir = '~/github/'+repo_name+'/'
        os.system(clone)
        os.system('cd '+ repo_dir)
        os.system('touch main.py\ntouch creds.py')

    #def openGit(self):


    #def clone(self):

bot = projectSync(c.user, c.pw )
