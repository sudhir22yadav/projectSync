import argparse
import os
from time import sleep
import creds as c
from selenium import webdriver
from selenium.webdriver.common import keys


class projectSync:
    def __init__(self, username, password, repo_name, desc):
        self.repo_name = repo_name
        self.desc = desc
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password

    def login(self):
        self.driver.get('https://github.com/')
        self.driver.find_element_by_xpath("//a[contains(@href,'/login')]").click()
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

    def create_repo(self):
        link = self.driver.find_element_by_class_name("dropdown-caret")
        sleep(.214)
        link.click()
        sleep(.380)
        create_new_repo = self.driver.find_element_by_xpath("//a[contains(@href,'/new')]")
        sleep(.60)
        create_new_repo.click()
        sleep(2)
        repo_name_field = self.driver.find_element_by_id('repository_name')
        sleep(.224)
        repo_name_field.send_keys(self.repo_name)
        sleep(.245)
        desc_field = self.driver.find_element_by_id('repository_description')
        desc_field.send_keys(self.desc)
        sleep(0.2158)
        visible = self.driver.find_element_by_id('repository_visibility_private')
        visible.click()
        sleep(.3568)
        repo_init = self.driver.find_element_by_id('repository_auto_init')
        repo_init.click()
        sleep(0.4485)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[1]/details/summary/span').click()
        sleep(0.145)
        ignore_field = self.driver.find_element_by_id('context-ignore-filter-field')
        ignore_field.send_keys('Python')
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[1]/details/details-menu/div[3]/div[1]/label[86]/span').click()
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[3]/button").click()
        sleep(4)
        self.driver.close()
        #sleep(3)

    # can predict the git url because it is predictable

    def clone(self):
        rep_link = 'https://' + self.username + ':' + c.token + '@github.com/sudhir22yadav/' + self.repo_name + '.git'
        clone = 'git clone ' + rep_link + ' ~/github/' + self.repo_name + '/'
        repo_dir = '~/github/' + self.repo_name + '/'
        os.system(clone)


# create parser
parser = argparse.ArgumentParser()
# add arguments to the parser
parser.add_argument('repo', help='Provide new project name')
parser.add_argument('desc', help='Provide a description')
args = parser.parse_args()

bot = projectSync(c.user, c.pw, args.repo, args.desc)
bot.login()
bot.create_repo()
bot.clone()
