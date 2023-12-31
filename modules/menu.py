import os, art, pick

def cls(): os.system('cls' if os.name=='nt' else 'clear')
    
class ParentMenu():
    
    def __init__(self, 
                 title:str="Title", 
                 options:dict[str, tuple[callable, dict[str, None]]]=None):
        
        self.title = title
        self.options = options
        
    def createMenu(self):
        
        options_list = [f"[{index+1}] {parametr}" for index, parametr in enumerate(self.options.keys())]
        
        title = art.text2art(self.title)
        index = 0

        while True:
            
            option, index = pick.pick(options_list, title, indicator='=>', default_index=index)
            
            func, kwargs = self.options.get(option[4:])
            
            if not func is None: 
                if kwargs: func.__call__(**kwargs)
                else: func.__call__()
            else: return 