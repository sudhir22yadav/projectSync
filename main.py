import argparse
import os
from time import sleep
import creds as c
from selenium import webdriver
from selenium.webdriver.common import keys


class projectSync:
    def __init__(self):
        #self.repo_name = repo_name
        #self.desc = desc
        self.driver = webdriver.Firefox()
        self.username = c.user
        self.password = c.pw
        self.visible = c.visible
        self.driver.get('https://github.com/')
        sleep(4)
        login_button = self.driver.find_element_by_xpath("//a[contains(@href,'/login')]")
        if login_button.is_displayed() is False:
            sleep(2)
            self.driver.find_element_by_tag_name('button').click()
            sleep(2)
            #login_button.click()
        else:
            login_button.click()
       
        login_field = self.driver.find_element_by_id("login_field")
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
        if link.is_displayed() is False:
            # dropdown button
            self.driver.find_element_by_tag_name('button').click()
            # profile
            self.driver.find_element_by_xpath("//a[contains(@href,'https://github.com/sudhir22yadav')]").click()
            # repository tab
            self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div[2]/nav/a[2]").click()
            sleep(2)
            # new repo green button
            self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div[3]/div[1]/form/div[2]/a").click()
        else:
            link.click()
            sleep(.380)
            create_new_repo = self.driver.find_element_by_xpath("//a[contains(@href,'/new')]")
            sleep(.60)
            create_new_repo.click()
            sleep(2)
        print('exited if loop')
        if self.visible == False:
            visible = self.driver.find_element_by_id('repository_visibility_private')
            visible.click()
        else:
            visible = self.driver.find_element_by_id('repository_visibility_public')
            visible.click()
bot = projectSync()
