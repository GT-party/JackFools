import os
from time import sleep
from modules.webdriver import AuditorDriver
from modules.menu import ParentMenu

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cls(): os.system('cls' if os.name=='nt' else 'clear')

class Guesspionage:
    
    def __init__(self) -> None:
        
        self.code: str = None
        self.entred: bool = False
        self.auditors: list[AuditorDriver] = []
    
    def open_code_input_menu(self):
        
        import art
        
        code = None
        
        while True:
            cls()
            print(art.text2art("Code input"))
            code = input("\nВведите код игры: ").upper()
            
            if code == "0": break
            
            if len(code) != 4: continue
            
            for code_letter in code:
                if code_letter not in ["Q", 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']: code = ""

            if code: break
        
        if code == "0": self.open_menu()
        else: 
            self.code = code
            return code
        
    def instanse_create(self, code: str, nickname):
            sleep(2)
            
            while True: 
                sleep(1)
                
                
                try:
                    driver = AuditorDriver()
                
                    driver.get(f"https://jackbox.fun?code={code}")
                    
                    usernameinput = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/input[2]")
                    usernameinput.send_keys(nickname)

                    button_join = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/form/fieldset/button")))
                    button_join.click()
            
                    button_join = WebDriverWait(driver, 2000000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div[20]/div/form/button[1]")))
                    button_join.click()
                    
                    driver.close()
                except: pass
                
            
    def create_auditors(self, count = 6, nickname = "Tedeshi"): 
        
        if not self.code: self.code = self.open_code_input_menu()
        
        import multiprocessing
        
        started_proccess:list[multiprocessing.Process] = []
        
        for _ in range(count): started_proccess.append(multiprocessing.Process(target=self.instanse_create, args=[self.code, nickname]))
        
        for p in started_proccess: p.start()
        
        self.auditors = started_proccess
        
        cls()
      
    
    def enter_to_the_game(self) -> None: pass
    
    def open_menu(self, back_function=None): 
        
        while True:
            full_menu_dict = {}
            
            if not self.code: full_menu_dict.update({"Ввести код игры": self.open_code_input_menu})
            elif not self.entred: full_menu_dict.update({"Войти в игру": None})
            else: full_menu_dict.update({"": None})
            
            
            if not self.auditors: full_menu_dict.update({"Инициировать фейк-зрителей": self.create_auditors})
            else: full_menu_dict.update({"Смухлевать выборку": None})
            
            
            full_menu_dict.update({"Назад": back_function})
            ParentMenu("Guesspionage", full_menu_dict).createMenu()
    