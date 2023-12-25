from selenium import webdriver
import os, logging

class DDOSdriver(webdriver.Chrome):
    
    def __init__(self, options = webdriver.ChromeOptions(), 
                 service = None, 
                 keep_alive: bool = True):
        
        options.headless = True
        options.add_argument('incognito')
        options.add_argument('--disable-gpu')
        
        super().__init__(options, service, keep_alive)
        
        self.minimize_window()