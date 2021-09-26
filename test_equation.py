from equation import FuncPlot
import numpy as np
import pytest


@pytest.mark.parametrize('min_x,max_x,func,x,y' , [
        (0,200,'2*x',np.linspace(0,200,200),2*np.linspace(0,200,200)),
        (-100,100,"5",np.linspace(-100,100,200),5*np.ones(200)),
        (-100,100,"x^2 + 3",np.linspace(-100,100,200),np.square(np.linspace(-100,100,200))+3)

])

def test_plot(min_x,max_x,func,x,y):
    data = FuncPlot(min_x,max_x,func)
    x_axis = data.x == x
    assert x_axis.all()
    y_axis = data.y == y
    assert y_axis.all()
