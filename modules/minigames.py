import os, art, multiprocessing
from time import sleep
from modules.webdriver import AuditorDriver, PlayerDriver
from modules.menu import ParentMenu

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cls(): os.system('cls' if os.name=='nt' else 'clear')

def open_code_input_menu():
    
    while True:
        cls()
        print(art.text2art("Code input"))
        code = input("\nВведите код игры [0 - чтобы назад]: ").upper()
        
        if code == "0": break
        elif len(code) != 4: continue
        
        for code_letter in code:
            if code_letter not in ["Q", 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']: continue

        if code: break
    
    if code == "0": return None
    else: return code

class BaseMinigame:
        
    code: str = None
    
    driver: PlayerDriver = None
    
    is_entred: bool = False
    auditors: list[multiprocessing.Process] = []

class Guesspionage(BaseMinigame):
        
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
            
                    button_join = WebDriverWait(driver, 200000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div/div/div[3]/div[20]/div/form/button[1]")))
                    button_join.click()
                    
                    driver.close()
                except: pass
                
            
    def create_auditors(self, count = 6, nickname = "Tedeshi_"): 
        
        if not self.code: self.code = open_code_input_menu()
        
        started_proccess:list[multiprocessing.Process] = []
        
        for _ in range(count): started_proccess.append(multiprocessing.Process(target=self.instanse_create, args=[self.code, nickname]))
        
        for p in started_proccess: p.start()
        
        self.auditors = started_proccess
        
        cls()
       
    def kill_auditors(self): 
        
        for audit in self.auditors: audit.kill()
            
        while [x for x in self.auditors if x.is_alive()] != []:
            
            cls()
            
            print(art.text2art("DDOSING..."))
            
            print(" ".join(["[ ]" if x.is_alive() else "[X]" for x in self.auditors ]))
            
            sleep(0.1)
        
        cls()
        
        self.auditors = []
    
    def enter_to_the_game(self) -> None: pass
    
    def answer_the_question(self):
        
        # Когда процент выбираешь не ты
        # Выбрать выше или ниже
        
        # Текст вопроса: /html/body/div/div/div[1]/div/div/div[3]/div[13]/div/p[1]
        # Какой был выбор отвечающего: /html/body/div/div/div[1]/div/div/div[3]/div[13]/div/p[2]
        
        # Кнопка намного выше: /html/body/div/div/div[1]/div/div/div[3]/div[13]/div/form/button[1]
        # Кнопка выше: /html/body/div/div/div[1]/div/div/div[3]/div[13]/div/form/button[2]
        # Кнопка ниже: /html/body/div/div/div[1]/div/div/div[3]/div[13]/div/form/button[3]
        # Кнопка ещё ниже: /html/body/div/div/div[1]/div/div/div[3]/div[13]/div/form/button[4]
        
        
        pass
    
    def open_menu(self, back_function=None): 
        
        full_menu_dict = {}
        
        if not self.is_entred: full_menu_dict.update({"Войти в игру": (None, None)})
        else: full_menu_dict.update({"Ответить правильно": (None, None)})
        
        if not self.auditors: full_menu_dict.update({"Инициировать фейк-зрителей": (self.create_auditors, None)})
        else: full_menu_dict.update({"Убрать зрителей": (self.kill_auditors, None)})
        
        full_menu_dict.update({"Назад": (None, None)})
        
        ParentMenu("Guesspionage", full_menu_dict).createMenu()

class TriviaMurder2(BaseMinigame):
    
    def __init__(self) -> None:
        
        super().__init__()
    
    def open_menu(self, back_function=None): 
        
        full_menu_dict = {}
        
        if not self.is_entred: full_menu_dict.update({"Войти в игру": (None, None)})
        else: full_menu_dict.update({"Ответить правильно": (None, None)})
        
        if not self.auditors: full_menu_dict.update({"Инициировать фейк-игроков": (None, None)})
        else: full_menu_dict.update({"Убрать зрителей": (None, None)})
        
        full_menu_dict.update({"Назад": (None, None)})
        
        ParentMenu("Guesspionage", full_menu_dict).createMenu()
