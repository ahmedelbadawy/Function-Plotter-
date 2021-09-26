from PyQt5 import QtWidgets , QtCore, QtGui
from pyqtgraph import PlotWidget, plot
import plotter
import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox
from equation import FuncPlot
import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow , plotter.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.widget_configuration(self.widget,'The plot')
        ## determine which char will be validate
        validator_func = QRegExpValidator(QRegExp(r'[0-9Xx+-/^()* ]+'))
        validator_int = QRegExpValidator(QRegExp(r'[0-9-+]+'))
        self.func.setValidator(validator_func)
        self.min.setValidator(validator_int)
        self.max.setValidator(validator_int)

        self.plot_button.clicked.connect(self.plot)
    ## function of plotting after pushing the plot button
    def plot(self):
        # if statement to check the errors and raise a pop up message
        if not self.func.text():
            self.pop_up("Enter the function!")
            self.text_clear()
        elif not self.max.text() or not self.min.text():
            self.pop_up("Enter Min and max values!")
            self.text_clear()
        elif float(self.min.text()) > float(self.max.text()) or float(self.min.text()) == float(self.max.text()):
            self.pop_up("The Max value must be greater.")
            self.text_clear()

        else:
            # plotting the function
            try:
                self.widget.clear()
                data = FuncPlot(float(self.min.text()),float(self.max.text()),self.func.text())
                self.widget.plot(data.x,data.y, pen = pg.mkPen(color=(255, 0, 0)))
                self.widget.setLimits(xMin = data.min, xMax= data.max,yMin =min(data.y), yMax =max(data.y) )
                self.widget.setXRange(data.min,data.max)
                self.widget.setYRange(min(data.y),max(data.y))
            except:
                self.pop_up("Enter validate function syntax!")
                self.text_clear()

        

    # func to generate pop up message
    def pop_up(self,error):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText('Error!')
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText(error)
        x = msg.exec_()

    def widget_configuration(self,widget,title):
        widget.showGrid(True, True, alpha=0.8)
        widget.setBackground('w') 
        widget.addLegend()
        widget.setTitle(title)
        widget.setXRange(0, 1000, padding=0)

    def text_clear(self):
        self.func.clear()
        self.max.clear()
        self.min.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
