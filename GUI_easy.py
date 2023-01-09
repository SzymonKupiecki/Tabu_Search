from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess
import sys
import numpy as np
import main_easy

hard_matrix = None
cable_vector = None
cost_tuples = None
result = None

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()
        self.plainTextEdit.setReadOnly(True)
        self.pushButton_2.clicked.connect(self.zapisz)
        self.pushButton.clicked.connect(self.start)
        self.p = None

    def message(self, s):
        self.plainTextEdit.appendPlainText(s)

    def zapisz(self):
        if self.textEdit.toPlainText() != "" and self.textEdit_2.toPlainText() != "" and self.textEdit_3.toPlainText() != "":
            self.pushButton.setEnabled(True)
            global hard_matrix
            hard_matrix = np.array(np.mat(self.textEdit.toPlainText()))
            global cable_vector
            cable_vector = np.array(np.mat(self.textEdit_2.toPlainText()))
            global cost_tuples
            cost_tuples = np.array(np.mat(self.textEdit_3.toPlainText()))
        else:
            self.pushButton.setEnabled(False)

    def start(self):
        if self.p is None:
            self.message("Executing process")
            global result
            result = main_easy.fun(hard_matrix, cable_vector, cost_tuples)
            self.p = QProcess()
            self.p.finished.connect(self.finish)
            self.p.start("python3", ['main_easy.py'])

    def finish(self):
        self.message("Process finished.")
        global result
        self.message(f"Result is:{result}")
        self.p = None

def window():
    app = QApplication([])
    win = MyWindow()
    app.exec_()

window()