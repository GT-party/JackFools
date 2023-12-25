import os, art, pick

def cls(): os.system('cls' if os.name=='nt' else 'clear')
    
class ParentMenu():
    
    def __init__(self, 
                 title:str="Title", 
                 options:dict[str, callable]=None):
        
        self.title = title
        self.options = options
        
    def createMenu(self):
        
        options_list = [f"[{index}] {parametr}" for index, parametr in enumerate(self.options.keys())]
        title = art.text2art(self.title)
        index = 0

        while True:
            
            option, index = pick.pick(options_list, title, indicator='=>', default_index=index)
            
            if self.options[" ".join(options_list[index].split(" ")[1:])] is None: return
            else: self.options[" ".join(options_list[index].split(" ")[1:])].__call__()
        