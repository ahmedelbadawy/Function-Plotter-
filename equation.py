import numpy as np

class FuncPlot():
    def __init__(self , min, max, func_str):
        self.min = min
        self.max = max
        self.func_str = func_str
        self.equation = self.func_str.lower().replace('^','**')
        self.x = np.arange(self.min ,self.max,(self.max-self.min )/200)
        x = self.x
        result = eval(self.equation)
        if isinstance(result,np.ndarray):
            self.y = result 
        else:
            self.y = result * np.ones(len(self.x))

    
        
    

