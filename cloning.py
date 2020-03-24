import argparse
import os
from time import sleep
import creds as c
from selenium import webdriver
from selenium.webdriver.common import keys


class ProjectSync:
    def __init__(self, username, password, repo_name, desc):
        self.repo_name = repo_name
        self.desc = desc
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self.login()

    def login(self):
        # Open up github.com webpage
        self.driver.get('https://github.com/')
        sleep(4)
        # Sign in Button if available
        login_button = self.driver.find_element_by_xpath("//a[contains(@href,'/login')]")

        # drop down menu to check sign in button
        # If sign in not available
        drop_button = self.driver.find_element_by_tag_name('button')
        # check if login button is visible or not
        if login_button.is_displayed() is False:
            sleep(2)
            drop_button.click()
            sleep(2)
            login_button.click()
        else:
            login_button.click()
        sleep(1)

        # opens up a new webpage
        # login field
        login_field = self.driver.find_element_by_id("login_field")
        # password field
        pw_field = self.driver.find_element_by_id("password")
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
        self.create_repo()

    def create_repo(self):
        # Profile Dashboard opens up
        # Dropdown menu
        dropdown = self.driver.find_element_by_class_name("dropdown-caret")
        drop_button = self.driver.find_element_by_tag_name('button')
        profile = self.driver.find_element_by_xpath("//a[contains(@href,'https://github.com/sudhir22yadav')]")
        # check if that '+' dropdown is visible or not
        if dropdown.is_displayed() is False:
            # dropdown button if '+' is not available
            drop_button.click()
            # profile
            profile.click()

            # New webpage opens up
            # repository tab
            repo_tab = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div[2]/nav/a[2]")
            repo_tab.click()
            sleep(2)
            # new repo green button
            new_repo_button = self.driver.find_element_by_xpath(
                "/html/body/div[4]/main/div/div[3]/div[3]/div[1]/form/div[2]/a")
            new_repo_button.click()
        else:
            # if '+' is available
            dropdown.click()
            sleep(.380)
            # create new repo
            create_new_repo = self.driver.find_element_by_xpath("//a[contains(@href,'/new')]")
            create_new_repo.click()
            sleep(2)

        # New webpage opens up
        sleep(.224)
        # repo field
        repo_name_field = self.driver.find_element_by_id('repository_name')
        repo_name_field.send_keys(self.repo_name)
        sleep(.245)
        # repo description field
        desc_field = self.driver.find_element_by_id('repository_description')
        desc_field.send_keys(self.desc)
        sleep(0.2158)
        # repo visibility choice
        visible = self.driver.find_element_by_id('repository_visibility_private')
        visible.click()
        sleep(.3568)
        # repo initialization
        repo_init = self.driver.find_element_by_id('repository_auto_init')
        repo_init.click()
        sleep(0.4485)
        # adding .gitignore
        add_gitignore = self.driver.find_element_by_xpath(
            '/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[1]/details/summary/span')
        add_gitignore.click()
        sleep(0.145)
        # adding python files to .gitignore
        ignore_field = self.driver.find_element_by_id('context-ignore-filter-field')
        ignore_field.send_keys('Python')
        set_ignore_field = self.driver.find_element_by_xpath(
            '/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[1]/details/details-menu/div[3]/div[1]/label[86]/span')
        set_ignore_field.click()
        # create repo button
        create_repo_button = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[3]/button")
        create_repo_button.click()
        sleep(4)
        # closing browser
        self.driver.close()
        self.clone()

    # system commands will run after this
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

bot = ProjectSync(c.user, c.pw, args.repo, args.desc)
