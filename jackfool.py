import os
from configs import Config

def cls(): os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    cls()
    
    if not os.path.exists("./temp"): os.mkdir("./temp")
    if not os.path.exists(Config.version_path): open(Config.version_path, "w").write(str(Config.version))
    
    
    if float(open(Config.version_path).read()) < Config.version:
        # if installed version don't equal actual version
        os.system("py -m pip install -r reqs.txt") #download new libs
        
    