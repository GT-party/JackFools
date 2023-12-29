import os, ujson
        
class Config():
    
    # JackBoxFools config
    version = 0.4
    version_path = "./temp/jbfools.version"
    
    # Screen parameteres
    width = 80
    
    # WebDriver config
    #webdriver_version_path = "./temp/webdriver.version"
    #webdriver_version = "120.0.6099.109"
    #webdriver_url = f"https://chromedriver.storage.googleapis.com/{webdriver_version}/chromedriver_win32.zip"
    #webdriver_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{webdriver_version}/win32/chrome-headless-shell-win32.zip"
    
class DDosConfig():
    
    nickname = "Tedeshi"
    
    restricted_parameters = ["path", "restricted_parameters"]
    path = "./temp/ddos.config"
    
    def __init__(self) -> None:
        
        if os.path.exists(self.path): 
    
            self.nickname = ujson.loads(open(self.path).read())["nickname"]
            
    def set_parameters(self, **kwargs):
        
        dictz:dict = ujson.loads(open(self.path, "r").read())
        
        with open(self.path, "w") as f:
            
            for key, value in kwargs.items():
                if key in "path": continue
                self.__setattr__(key, value)
                dictz.update({key: value})
            
            f.write(ujson.dumps(dictz))
                