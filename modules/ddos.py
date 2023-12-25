
import os, ujson

from modules.menu import ParentMenu

def cls(): os.system('cls' if os.name=='nt' else 'clear')
    
class JBDdos():
    
    def __init__(self):
        from modules.configs import DDosConfig
        
        self.config = DDosConfig()
        
        if not os.path.exists(self.config.path): open(self.config.path, "w").write(ujson.dumps({"nickname": self.input_nickname()}))
        else: self.config.nickname = ujson.loads(open(self.config.path, "r").read())["nickname"]
        
    def open_menu(self, back_function):
        ParentMenu("DDOS", {"Назад", back_function})
    
    def input_nickname(self):
        
        nickname = None
        
        while True:
            
            if not nickname: pass
            elif not (len(nickname) < 11 and len(nickname) > 0): 
                print(f"Длина никнейма должна быть от 1 до 11 символов...[{nickname}]")
            else: return nickname
            
            nickname = input(f"DDOS никнейм [Enter, чтобы установить по дефолту: {self.config.nickname}]: ")
        