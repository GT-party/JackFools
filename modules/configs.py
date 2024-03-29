
class Config():
    
    # JackBoxFools config
    version = 0.52
    version_path = "./temp/jbfools.version"
    
    # Screen parameteres
    width = 80
    
    # WebDriver config
    webdriver_version_path = "./temp/webdriver.version"
    webdriver_version = "120.0.6099.109"
    
    webdriver_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{webdriver_version}/win32/chromedriver-win32.zip"
    
class DDosConfig():
    
    nickname = "Tedeshi"
    
    restricted_parameters = ["path", "restricted_parameters"]
    path = "./temp/ddos.config"
    
    def __init__(self) -> None:
        import os, ujson
        
        if os.path.exists(self.path): self.nickname = ujson.loads(open(self.path).read())["nickname"]
        else: open(self.path, "w").write(ujson.dumps({"nickname": self.nickname}))
            
    def set_parameters(self, **kwargs):
        import ujson
        dictz:dict = ujson.loads(open(self.path, "r").read())
        
        with open(self.path, "w") as f:
            
            for key, value in kwargs.items():
                if key in "path": continue
                self.__setattr__(key, value)
                dictz.update({key: value})
            
            f.write(ujson.dumps(dictz))
                