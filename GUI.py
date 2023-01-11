from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess
import sys
import numpy as np
import main

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
            file = open("hard_matrix.txt", "w")
            file.write(self.textEdit.toPlainText())
            file.close
            file = open("cable_vector.txt", "w")
            file.write(self.textEdit_2.toPlainText())
            file.close
            file = open("cost_tuples.txt", "w")
            file.write(self.textEdit_3.toPlainText())
            file.close
            file = open("tabu.txt", "w")
            file.write(self.textEdit_4.toPlainText())
            file.close
            file = open("mid_mem.txt", "w")
            file.write(self.textEdit_5.toPlainText())
            file.close
            file = open("iteration.txt", "w")
            file.write(self.textEdit_6.toPlainText())
            file.close
        else:
            self.pushButton.setEnabled(False)

    def start(self):
        if self.p is None:
            self.message("Executing process")
            self.p = QProcess()
            self.p.finished.connect(self.finish)
            self.p.start("python3", ['main.py'])

    def finish(self):
        main.fun()
        file = open("res.txt", "r")
        result = file.read()
        file.close
        self.message(f"Result is:{result}")
        self.photo.setPixmap(QtGui.QPixmap("plot.png"))
        self.message("Process finished.")
        self.p = None

def window():
    app = QApplication([])
    win = MyWindow()
    app.exec_()

window()