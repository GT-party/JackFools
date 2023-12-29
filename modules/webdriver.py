from selenium import webdriver
import os


class BaseDriver(webdriver.Chrome):
    
    def __init__(self, is_visible = False, options = webdriver.ChromeOptions(),  service = webdriver.ChromeService(executable_path=None, log_path=os.devnull) ):
        
        if not is_visible:
            options.headless = True
            options.add_argument('incognito')
            options.add_argument('--disable-gpu')
            self.minimize_window()
        
        super().__init__(options, service)


class PlayerDriver(BaseDriver):
    
    def __init__(self): super().__init__(is_visible=True)
    

class AuditorDriver(BaseDriver):
    
    def __init__(self): super().__init__()