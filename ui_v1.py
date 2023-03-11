from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *

import test_func
import var1
import var10
import var10_period
import var15
import var15_period
import var1_period
import var3
import var3_period
from test_func import *
from var1 import *
from var1_period import *
from var3 import *
from var3_period import *
from var10 import *
from var10_period import *
from var15 import *
from var15_period import *


class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    N = 10

    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    flag6 = False
    flag7 = False

    def set_N(self, N):
        self.N = N
        print(N)

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot_var1(self):
        function = getdata_var1(self.N, 2, 4)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_testFunc(self):
        function = getdata_testFunc(self.N, -1, 1)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var1_period(self):
        function = getdata_var1_period(self.N, 2, 4)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var3(self):
        function = getdata_var3(self.N, 0, 2)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var3_period(self):
        function = getdata_var3_period(self.N, 0, 2)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var10(self):
        function = getdata_var10(self.N, 1, np.pi)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var10_period(self):
        function = getdata_var10_period(self.N, 1, np.pi)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var15(self):
        function = getdata_var15(self.N, 0, np.pi)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()

    def plot_var15_period(self):
        function = getdata_var15_period(self.N, 0, np.pi)

        x = function[0]
        y1 = function[1]
        y2 = function[2]
        y3 = function[3]
        y4 = function[5]
        y5 = function[7]
        y6 = function[8]
        y7 = function[9]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        if self.flag1 == True:
            ax.plot(x, y1, linewidth=0.7, linestyle='-', color='red')
        if self.flag2 == True:
            ax.plot(x, y2, linewidth=0.7, linestyle='-', color='blue')
        if self.flag3 == True:
            ax.plot(x, y3, linewidth=0.7, linestyle='-', color='purple')
        if self.flag4 == True:
            ax.plot(x, y4, linewidth=0.7, linestyle='-', color='brown')
        if self.flag5 == True:
            ax.plot(x, y5, linewidth=0.7, linestyle='-', color='yellow')
        if self.flag6 == True:
            ax.plot(x, y6, linewidth=0.7, linestyle='-', color='orange')
        if self.flag7 == True:
            ax.plot(x, y7, linewidth=0.7, linestyle='-', color='black')
        self.canvas.draw()


'''''
    def plot(self, function_index):

        functions = {
            1: getdata_var1(10,2,4),
            2: getdata_var3(10,2,4),
        }

        x = functions[function_index][0]
        y = functions[function_index][1]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')

        ax.plot(x, y, linewidth=0.7, linestyle='-', color='red')
        self.canvas.draw()
'''''


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1760, 920)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graph_widget = PlotWidget()
        # self.graph_widget = QtWidgets.QWidget(self.centralwidget)
        self.graph_widget.setGeometry(QtCore.QRect(689, 10, 1061, 591))
        self.graph_widget.setStyleSheet("border: red;\n"
                                        "background-color: #b5b5b5;")
        self.graph_widget.setObjectName("graph_widget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 510, 661, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(PlotWidget.N)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setColumnWidth(0, 15)

        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(690, 610, 1061, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(11)
        self.tableWidget_2.setRowCount(PlotWidget.N)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)

        self.tableWidget_2.setColumnWidth(0, 15)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(362, 10, 311, 257))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tasks_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.tasks_comboBox.setObjectName("tasks_comboBox")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.tasks_comboBox.addItem("")
        self.verticalLayout.addWidget(self.tasks_comboBox)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spline_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.spline_graph.setObjectName("spline_graph")
        self.verticalLayout.addWidget(self.spline_graph)
        self.func_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.func_graph.setObjectName("func_graph")
        self.verticalLayout.addWidget(self.func_graph)
        self.df_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.df_graph.setObjectName("df_graph")
        self.verticalLayout.addWidget(self.df_graph)
        self.d2f_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.d2f_graph.setObjectName("d2f_graph")
        self.verticalLayout.addWidget(self.d2f_graph)
        self.rSpline_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.rSpline_graph.setObjectName("rSpline_graph")
        self.verticalLayout.addWidget(self.rSpline_graph)
        self.drSpline_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.drSpline_graph.setObjectName("drSpline_graph")
        self.verticalLayout.addWidget(self.drSpline_graph)
        self.d2rSpline_graph = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.d2rSpline_graph.setObjectName("d2rSpline_graph")
        self.verticalLayout.addWidget(self.d2rSpline_graph)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.TitleImage = QtWidgets.QLabel(self.centralwidget)
        self.TitleImage.setGeometry(QtCore.QRect(10, 10, 331, 141))
        self.TitleImage.setAutoFillBackground(False)
        self.TitleImage.setText("")
        self.TitleImage.setPixmap(QtGui.QPixmap("img/test.png"))
        self.TitleImage.setScaledContents(True)
        self.TitleImage.setObjectName("TitleImage")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 270, 241, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.n_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.n_line.setObjectName("n_line")
        self.horizontalLayout.addWidget(self.n_line)
        self.n_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.n_pb.setStyleSheet("")
        self.n_pb.setObjectName("n_pb")
        self.horizontalLayout.addWidget(self.n_pb)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 210, 331, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.n_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.n_label.setObjectName("n_label")
        self.gridLayout.addWidget(self.n_label, 1, 1, 1, 1)
        self.N_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.N_label.setObjectName("N_label")
        self.gridLayout.addWidget(self.N_label, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("margin-left: 20px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 661, 194))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rSpline = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.rSpline.setStyleSheet("background-color: white;\n"
                                   "position: relative;\n"
                                   "z-index: 10;")
        self.rSpline.setIndent(2)
        self.rSpline.setObjectName("rSpline")
        self.gridLayout_2.addWidget(self.rSpline, 1, 1, 1, 1)
        self.rSplineX = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.rSplineX.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.rSplineX.setIndent(2)
        self.rSplineX.setObjectName("rSplineX")
        self.gridLayout_2.addWidget(self.rSplineX, 1, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.label_16.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_16.setIndent(2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("img/norm1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setIndent(2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("img/norm2.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setIndent(2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setIndent(2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 2, 1, 1)
        self.drSplineX = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.drSplineX.setStyleSheet("background-color: white;\n"
                                     "position: relative;\n"
                                     "z-index: 10;")
        self.drSplineX.setIndent(2)
        self.drSplineX.setObjectName("drSplineX")
        self.gridLayout_2.addWidget(self.drSplineX, 3, 3, 1, 1)
        self.drSpline = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.drSpline.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.drSpline.setIndent(2)
        self.drSpline.setObjectName("drSpline")
        self.gridLayout_2.addWidget(self.drSpline, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("img/norm3.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setIndent(2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 5, 0, 1, 1)
        self.d2rSpline = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.d2rSpline.setStyleSheet("background-color: white;\n"
                                     "position: relative;\n"
                                     "z-index: 10;")
        self.d2rSpline.setIndent(2)
        self.d2rSpline.setObjectName("d2rSpline")
        self.gridLayout_2.addWidget(self.d2rSpline, 5, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_22.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.label_22.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_22.setIndent(2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 5, 2, 1, 1)
        self.d2rSpline_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.d2rSpline_2.setStyleSheet("background-color: white;\n"
                                       "position: relative;\n"
                                       "z-index: 10;")
        self.d2rSpline_2.setIndent(2)
        self.d2rSpline_2.setObjectName("d2rSpline_2")
        self.gridLayout_2.addWidget(self.d2rSpline_2, 5, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: white;\n"
                                   "position: relative;\n"
                                   "z-index: 10;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setIndent(2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 4)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setIndent(2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 4)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: white;\n"
                                    "position: relative;\n"
                                    "z-index: 10;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setIndent(2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1760, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.l = QVBoxLayout(self.centralwidget)
        self.bl = QHBoxLayout(self.centralwidget)

        self.l2 = QVBoxLayout(self.graph_widget)
        self.l.addWidget(self.graph_widget)
        self.l2.addWidget(self.graph_widget)

        self.message = QMessageBox()

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "i"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Xi-1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Xi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ai"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "bi"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ci"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "di"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "j"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "xj"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "F(xj)"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "S(xj)"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "|F(xj)-S(xj)|"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F\'(xj)"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "S\'(xj)"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "|F\'(xj)-S\'(xj)|"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "F\'\'(xj)"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S\'\'(xj)"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "|F\'\'(xj)-S\'\'(xj)|"))
        self.tasks_comboBox.setItemText(0, _translate("MainWindow", "Тестовая задача"))
        self.tasks_comboBox.setItemText(1, _translate("MainWindow", "Вариант №1"))
        self.tasks_comboBox.setItemText(2, _translate("MainWindow", "Вариант №1 (периодическая)"))
        self.tasks_comboBox.setItemText(3, _translate("MainWindow", "Вариант №3"))
        self.tasks_comboBox.setItemText(4, _translate("MainWindow", "Вариант №3 (периодическая)"))
        self.tasks_comboBox.setItemText(5, _translate("MainWindow", "Вариант №10"))
        self.tasks_comboBox.setItemText(6, _translate("MainWindow", "Вариант №10 (периодическая)"))
        self.tasks_comboBox.setItemText(7, _translate("MainWindow", "Вариант №15"))
        self.tasks_comboBox.setItemText(8, _translate("MainWindow", "Вариант №15 (периодическая)"))
        self.label.setText(_translate("MainWindow", "Показать:"))
        self.spline_graph.setText(_translate("MainWindow", "График сплайна"))
        self.func_graph.setText(_translate("MainWindow", "График функции"))
        self.df_graph.setText(_translate("MainWindow", "График производной"))
        self.d2f_graph.setText(_translate("MainWindow", "График второй производной"))
        self.rSpline_graph.setText(_translate("MainWindow", "График погрешности сплайна"))
        self.drSpline_graph.setText(_translate("MainWindow", "График погрешности первой производной"))
        self.d2rSpline_graph.setText(_translate("MainWindow", "График погрешности второй производной "))
        self.label_3.setText(_translate("MainWindow", "Число разбиений:"))
        self.n_line.setText(_translate("MainWindow", "10"))
        self.n_pb.setText(_translate("MainWindow", "OK"))
        self.label_6.setText(_translate("MainWindow", "Контрольная сетка: N ="))
        self.label_5.setText(_translate("MainWindow", "Сетка сплайна: n ="))
        self.n_label.setText(_translate("MainWindow", "0"))
        self.N_label.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Справка"))
        self.gridLayoutWidget_2.setStyleSheet(_translate("MainWindow", "background-color: white;\n"
                                                                       "position: relative;\n"
                                                                       "z-index: 10;"))
        self.rSpline.setText(_translate("MainWindow", "0"))
        self.rSplineX.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "при x = "))
        self.label_14.setStyleSheet(_translate("MainWindow", "background-color: white;\n"
                                                             "position: relative;\n"
                                                             "z-index: 10;"))
        self.label_12.setText(_translate("MainWindow", "при x = "))
        self.drSplineX.setText(_translate("MainWindow", "0"))
        self.drSpline.setText(_translate("MainWindow", "0"))
        self.label_20.setStyleSheet(_translate("MainWindow", "background-color: white;\n"
                                                             "position: relative;\n"
                                                             "z-index: 10;"))
        self.d2rSpline.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "при x = "))
        self.d2rSpline_2.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Погрешность сплайна на контрольной сетке"))
        self.label_18.setText(_translate("MainWindow", "Погрешность производной на контрольной сетке"))
        self.label_19.setText(_translate("MainWindow", "Погрешность второй производной на контрольной сетке"))

        self.n_pb.clicked.connect(lambda: PlotWidget.set_N(PlotWidget, int(self.n_line.text())))
        # self.n_pb.clicked.connect(lambda: self.graph_widget.plot_var1())
        self.n_pb.clicked.connect(self.PlotGraph)
        self.n_pb.clicked.connect(self.setTable)
        self.n_pb.clicked.connect(self.setInfo)
        self.tasks_comboBox.currentIndexChanged.connect(self.ClearCheckBox)

        self.spline_graph.toggled.connect(self.onCheckBox_Toggled)
        self.func_graph.toggled.connect(self.onCheckBox_Toggled)
        self.df_graph.toggled.connect(self.onCheckBox_Toggled)
        self.d2f_graph.toggled.connect(self.onCheckBox_Toggled)
        self.rSpline_graph.toggled.connect(self.onCheckBox_Toggled)
        self.drSpline_graph.toggled.connect(self.onCheckBox_Toggled)
        self.d2rSpline_graph.toggled.connect(self.onCheckBox_Toggled)

    def PlotGraph(self):
        print(self.tasks_comboBox.currentIndex())
        if self.tasks_comboBox.currentIndex() == 0:
            self.graph_widget.plot_testFunc()
        if self.tasks_comboBox.currentIndex() == 1:
            self.graph_widget.plot_var1()
        if self.tasks_comboBox.currentIndex() == 2:
            self.graph_widget.plot_var1_period()
        if self.tasks_comboBox.currentIndex() == 3:
            self.graph_widget.plot_var3()
        if self.tasks_comboBox.currentIndex() == 4:
            self.graph_widget.plot_var3_period()
        if self.tasks_comboBox.currentIndex() == 5:
            self.graph_widget.plot_var10()
        if self.tasks_comboBox.currentIndex() == 6:
            self.graph_widget.plot_var10_period()
        if self.tasks_comboBox.currentIndex() == 7:
            self.graph_widget.plot_var15()
        if self.tasks_comboBox.currentIndex() == 8:
            self.graph_widget.plot_var15_period()

    def ClearCheckBox(self):
        if self.tasks_comboBox.currentIndex() == 0:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/test.png"))
        if self.tasks_comboBox.currentIndex() == 1:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var1.PNG"))
        if self.tasks_comboBox.currentIndex() == 2:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var1p.PNG"))
        if self.tasks_comboBox.currentIndex() == 3:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var3.PNG"))
        if self.tasks_comboBox.currentIndex() == 4:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var3p.PNG"))
        if self.tasks_comboBox.currentIndex() == 5:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var10.PNG"))
        if self.tasks_comboBox.currentIndex() == 6:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var10p.PNG"))
        if self.tasks_comboBox.currentIndex() == 7:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var15.PNG"))
        if self.tasks_comboBox.currentIndex() == 8:
            self.TitleImage.setPixmap(QtGui.QPixmap("img/var15p.PNG"))

        self.graph_widget.figure.clear()
        self.graph_widget.canvas.draw()

    def setTable(self):

        if self.tasks_comboBox.currentIndex() == 0:
            List = test_func.getdata_testFunc(PlotWidget.N, -1, 1)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 1:
            List = var1.getdata_var1(PlotWidget.N, 2, 4)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 2:
            List = var1_period.getdata_var1_period(PlotWidget.N, 2, 4)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 3:
            List = var3.getdata_var3(PlotWidget.N, 0, 2)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 4:
            List = var3_period.getdata_var3_period(PlotWidget.N, 0, 2)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 5:
            List = var10.getdata_var10(PlotWidget.N, 1, np.pi)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 6:
            List = var10_period.getdata_var10_period(PlotWidget.N, 1, np.pi)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 7:
            List = var15.getdata_var15(PlotWidget.N, 0, np.pi)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

        if self.tasks_comboBox.currentIndex() == 8:
            List = var15_period.getdata_var15_period(PlotWidget.N, 0, np.pi)
            self.tableWidget.setRowCount(len(List[14]) - 1)
            self.tableWidget_2.setRowCount(len(List[0]))
            for i in range(len(List[0])):
                self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(List[0][i])))
                self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(List[2][i])))
                self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(List[1][i])))
                self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(List[7][i])))
                self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(List[4][i])))
                self.tableWidget_2.setItem(i, 6, QTableWidgetItem(str(List[3][i])))
                self.tableWidget_2.setItem(i, 7, QTableWidgetItem(str(List[8][i])))
                self.tableWidget_2.setItem(i, 8, QTableWidgetItem(str(List[6][i])))
                self.tableWidget_2.setItem(i, 9, QTableWidgetItem(str(List[5][i])))
                self.tableWidget_2.setItem(i, 10, QTableWidgetItem(str(List[9][i])))

            for i in range(1, len(List[14])):
                self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(str(i)))
                self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(str(List[14][i - 1])))
                self.tableWidget.setItem(i - 1, 2, QTableWidgetItem(str(List[14][i])))
                self.tableWidget.setItem(i - 1, 3, QTableWidgetItem(str(List[10][i])))
                self.tableWidget.setItem(i - 1, 4, QTableWidgetItem(str(List[11][i - 1])))
                self.tableWidget.setItem(i - 1, 5, QTableWidgetItem(str(List[12][i])))
                self.tableWidget.setItem(i - 1, 6, QTableWidgetItem(str(List[13][i - 1])))

    def setInfo(self):
        self.n_label.setText('0')
        self.N_label.setText('0')
        self.rSpline.setText('0')
        self.drSpline.setText('0')
        self.d2rSpline.setText('0')
        self.rSplineX.setText('0')
        self.drSplineX.setText('0')
        self.d2rSpline_2.setText('0')

        if self.tasks_comboBox.currentIndex() == 0:
            List = test_func.getdata_testFunc(PlotWidget.N, -1, 1)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 1:
            List = var1.getdata_var1(PlotWidget.N, 2, 4)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 2:
            List = var1_period.getdata_var1_period(PlotWidget.N, 2, 4)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 3:
            List = var3.getdata_var3(PlotWidget.N, 0, 2)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 4:
            List = var3_period.getdata_var3_period(PlotWidget.N, 0, 2)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 5:
            List = var10.getdata_var10(PlotWidget.N, 1, np.pi)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 6:
            List = var10_period.getdata_var10_period(PlotWidget.N, 1, np.pi)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 7:
            List = var15.getdata_var15(PlotWidget.N, 0, np.pi)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

        if self.tasks_comboBox.currentIndex() == 8:
            List = var15_period.getdata_var15_period(PlotWidget.N, 0, np.pi)
            self.n_label.setText(str(len(List[14])))
            self.N_label.setText(str(len(List[0])))

            self.rSpline.setText(str(max(List[7])))
            self.rSplineX.setText(str(List[0][List[7].index(max(List[7]))]))

            self.drSpline.setText(str(max(List[8])))
            self.drSplineX.setText(str(List[0][List[8].index(max(List[8]))]))

            self.d2rSpline.setText(str(max(List[9])))
            self.d2rSpline_2.setText(str(List[0][List[9].index(max(List[9]))]))

    def onCheckBox_Toggled(self):
        if self.spline_graph.isChecked():
            PlotWidget.flag1 = True
            # print(PlotWidget.flag1)
        else:
            PlotWidget.flag1 = False
            # print(PlotWidget.flag1)

        if self.func_graph.isChecked():
            PlotWidget.flag2 = True
            # print(PlotWidget.flag2)
        else:
            PlotWidget.flag2 = False
            # print(PlotWidget.flag2)

        if self.df_graph.isChecked():
            PlotWidget.flag3 = True
            # print(PlotWidget.flag3)
        else:
            PlotWidget.flag3 = False
            # print(PlotWidget.flag3)

        if self.d2f_graph.isChecked():
            PlotWidget.flag4 = True
            # print(PlotWidget.flag4)
        else:
            PlotWidget.flag4 = False
            # print(PlotWidget.flag4)

        if self.rSpline_graph.isChecked():
            PlotWidget.flag5 = True
            # print(PlotWidget.flag5)
        else:
            PlotWidget.flag5 = False
            # print(PlotWidget.flag5)

        if self.drSpline_graph.isChecked():
            PlotWidget.flag6 = True
            # print(PlotWidget.flag6)
        else:
            PlotWidget.flag6 = False
            # print(PlotWidget.flag6)

        if self.d2rSpline_graph.isChecked():
            PlotWidget.flag7 = True
            # print(PlotWidget.flag7)
        else:
            PlotWidget.flag7 = False
            # print(PlotWidget.flag7)
        # print()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
