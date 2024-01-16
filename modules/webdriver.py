from selenium import webdriver
import os, time

class NewBaseDriver(webdriver.Edge):
    
    def __init__(self,
                 is_visible = False, 
                 options = webdriver.EdgeOptions(), 
                 service = webdriver.EdgeService(executable_path="./temp/msedgedriver.exe", 
                                                 log_path=os.devnull)):
        
        
        if not is_visible:
        
            options.add_argument('-headless')  # Установите голову в режим без головы (т.е. невидимый)
            options.add_argument("--log-level=3")

        super().__init__(options, service)
        #print ("\033[A                                                                                                \033[A")
        if not is_visible: self.minimize_window()

class BaseDriver(webdriver.Chrome):
    
    def __init__(self, 
                 is_visible = False, 
                 options = webdriver.ChromeOptions(), 
                 service = webdriver.ChromeService(executable_path=None, log_path=os.devnull, log_output=os.devnull)):
        import logging
        
        if not is_visible or True:
            options.headless = True
            import logging
            
            logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
            logger.setLevel(logging.FATAL)
            
            options.add_argument('--incognito')
            options.add_argument("--silent")
            options.add_argument('--disable-gpu')
            options.add_argument('--headless=new')
            options.add_argument("--log-level=3")
            options.add_argument('--no-sandbox') # Bypass OS security model
            options.add_argument('--disable-infobars')
            options.add_argument("--disable-extensions")
            
            # options.set_capability("browser", "OFF")
            # options.set_capability("driver", "OFF")
            # options.set_capability("performance", "OFF")
            # options.set_capability("server", "OFF")

            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
        super().__init__(options, service)
        #print ("\033[A                                                                                                \033[A")
        if not is_visible: self.minimize_window()


class PlayerDriver(BaseDriver):
    
    def __init__(self): super().__init__(is_visible=True)
    

class AuditorDriver(BaseDriver):
    
    def __init__(self): super().__init__()