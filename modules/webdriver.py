from selenium import webdriver
import os

class DDOSdriver(webdriver.Chrome):
    
    def __init__(self, options = webdriver.ChromeOptions(), 
                 service = webdriver.ChromeService(executable_path=None, #r"./temp/chrome-headless-shell-win32/chrome-headless-shell.exe", 
                                                   log_path=os.devnull), 
                 keep_alive: bool = True):
        
        options.headless = True
        options.add_argument('incognito')
        options.add_argument('--disable-gpu')
        
        super().__init__(options, service, keep_alive)
        
        self.minimize_window()
        
class AuditorDriver(webdriver.Chrome):
    
    def __init__(self, is_visible = False,
                 options = webdriver.ChromeOptions(), 
                 service = webdriver.ChromeService(executable_path=None, #r"./temp/chrome-headless-shell-win32/chrome-headless-shell.exe", 
                                                   log_path=os.devnull), 
                 keep_alive: bool = True):
        
        options.headless = not is_visible
        if not is_visible: options.add_argument('--disable-gpu')
        options.add_argument('incognito')
        
        super().__init__(options, service, keep_alive)
        
        self.minimize_window()