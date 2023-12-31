from selenium import webdriver
import os


class BaseDriver(webdriver.Chrome):
    
    def __init__(self, 
                 is_visible = False, 
                 options = webdriver.ChromeOptions(), 
                 service = webdriver.ChromeService(executable_path=None, log_path=os.devnull) ):
        import logging
        
        if not is_visible:
            options.headless = True
            options.add_argument('incognito')
            options.add_argument('--disable-gpu')
            options.add_argument("--log-level=5")
            
        super().__init__(options, service)
        self.minimize_window()


class PlayerDriver(BaseDriver):
    
    def __init__(self): super().__init__(is_visible=True)
    

class AuditorDriver(BaseDriver):
    
    def __init__(self): super().__init__()