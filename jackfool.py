import os, sys
from modules.configs import Config

def cls(): os.system('cls' if os.name=='nt' else 'clear')

def init():
    cls()
    # initial checks
    if not os.path.exists("./temp"): os.mkdir("./temp")
    if not os.path.exists(Config.version_path): open(Config.version_path, "w").write(str(Config.version))
    # if not os.path.exists(Config.webdriver_version_path): open(Config.webdriver_version_path, "w").write(str(Config.webdriver_version))
    
    
    if float(open(Config.version_path).read()) < Config.version:
        # if installed JBFools version don't equal actual version
        os.system("py -m pip install -r reqs.txt") #install new libs
        open(Config.version_path, "w").write(str(Config.version)) # Update the local version
    
    # if open(Config.webdriver_version_path).read() != Config.webdriver_version or \
    #     (not os.path.exists("./temp/chromedriver-win32")):
        
    #     # if installed WebDriver version don't equal actual version
    #     from modules.downloader import download
    #     from zipfile import ZipFile
        
    #     download([Config.webdriver_url], dest_dir="./temp") # Download archive with webdriver
    #     with ZipFile("./temp/" + Config.webdriver_url.split("/")[-1], "r") as zfile: zfile.extractall("./temp") # unpack archive
    #     os.remove("./temp/" + Config.webdriver_url.split("/")[-1]) # Delete unpacked archive
    #     open(Config.webdriver_version_path, "w").write(Config.webdriver_version) # Update the local version
    


if __name__ == "__main__":
    
    if "-v" in sys.argv or "--version" in sys.argv: print("JBfools actual: " + str(Config.version) + " (local: " + open(Config.version_path).read() + ")" + \
                                                          "\nWebDriver actual: " + str(Config.webdriver_version) + " (local: " + open(Config.webdriver_version_path).read() + ")"
                                                        )
    #elif:
    else: 
        
        init()
        
        if "--ddos" in [_.lower() for _ in sys.argv]: 
            from modules.ddos import JBDdos
            
            JBDdos().open_menu(None)