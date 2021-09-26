import numpy as np

class FuncPlot():
    def __init__(self , min_x, max_x, func_str):
        self.min = min_x
        self.max = max_x
        self.func_str = func_str
        self.equation = self.func_str.lower().replace('^','**')
        self.x = np.linspace(min_x,max_x,200)
        x = self.x
        result = eval(self.equation)
        if isinstance(result,np.ndarray):
            self.y = result 
        else:
            self.y = result * np.ones(len(self.x))

    
        
    

