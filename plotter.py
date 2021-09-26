# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 710)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/line-chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.widget.setFont(font)
        self.widget.setWhatsThis("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.func = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setStrikeOut(False)
        font.setKerning(True)
        self.func.setFont(font)
        self.func.setWhatsThis("")
        self.func.setText("")
        self.func.setObjectName("func")
        self.verticalLayout.addWidget(self.func)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.min = QtWidgets.QLineEdit(self.centralwidget)
        self.min.setObjectName("min")
        self.horizontalLayout.addWidget(self.min)
        self.max = QtWidgets.QLineEdit(self.centralwidget)
        self.max.setObjectName("max")
        self.horizontalLayout.addWidget(self.max)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plot_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.plot_button.sizePolicy().hasHeightForWidth())
        self.plot_button.setSizePolicy(sizePolicy)
        self.plot_button.setMinimumSize(QtCore.QSize(0, 5))
        font = QtGui.QFont()
        font.setFamily("URW Bookman [urw]")
        font.setPointSize(20)
        self.plot_button.setFont(font)
        self.plot_button.setObjectName("plot_button")
        self.verticalLayout.addWidget(self.plot_button)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotter"))
        self.widget.setStatusTip(_translate("MainWindow", "The graph"))
        self.func.setStatusTip(_translate("MainWindow", "the function"))
        self.func.setPlaceholderText(_translate("MainWindow", "Enter a function of x, e.g., 5*x^3 + 2*x."))
        self.min.setStatusTip(_translate("MainWindow", "The Min value of x"))
        self.min.setPlaceholderText(_translate("MainWindow", "Min value of x"))
        self.max.setStatusTip(_translate("MainWindow", "The Max value of x"))
        self.max.setPlaceholderText(_translate("MainWindow", "Max value of x"))
        self.plot_button.setStatusTip(_translate("MainWindow", "Plot the function"))
        self.plot_button.setText(_translate("MainWindow", "Plot"))
        self.plot_button.setShortcut(_translate("MainWindow", "Return"))
from pyqtgraph import PlotWidget
